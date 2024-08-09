"""ucan.core.token module."""

from __future__ import annotations

import datetime as dt
import secrets
import typing_extensions as te

import pydantic as pyd

from ucan.core.capability import Capability
from ucan.core.plugins import DidableKey, Plugins
from ucan.core.types import Ucan, UcanHeader, UcanPayload
from ucan.encoding import Base64UrlEncoder
from ucan.schemas import DatetimeAsIntTimestamp, DidString, validate_call
from ucan.utils import aware_utcnow


__all__ = (
    # constants
    "TYPE",
    "VERSION",
    # exceptions
    "ProofError",
    # utils
    "is_expired",
    "is_too_early",
    # implementations
    "build_payload",
    "TokenBuildFunc",
    "build",
    "TokenSignFunc",
    "sign",
    "TokenSignWithKeyPairFunc",
    "sign_with_keypair",
    "TokenParseFunc",
    "parse",
    "TokenValidateFunc",
    "validate",
    "TokenValidateProofFunc",
    "validate_proofs",
)


# Constants

TYPE = "JWT"
VERSION = {"major": 0, "minor": 8, "patch": 1}


# typing

SignFuncCallback = te.Callable[[bytes], bytes]


# exceptions


class ProofError(Exception):
    """Exception related to proofs."""


# utils


def is_expired(ucan: Ucan) -> bool:
    """Check if a UCAN is expired.

    Args:
        ucan (Ucan): The UCAN to validate.

    Returns:
        bool: Whether the token is expired, i.e. current time is
            less than or equals to UCAN's `exp` value.
    """
    return ucan.payload.exp <= aware_utcnow()


def is_too_early(ucan: Ucan) -> bool:
    """Check if a UCAN is not active yet.

    Args:
        ucan (Ucan): The UCAN to validate.

    Returns:
        bool: Whether the token is active yet, i.e. current time is
            greater than the UCAN's `nbf` value.
    """
    if ucan.payload.nbf is None:
        return False

    return ucan.payload.nbf > aware_utcnow()


# implementations


# build payload


@validate_call
def build_payload(  # noqa: PLR0913
    issuer: DidString,
    audience: DidString,
    capabilities: list[Capability],
    *,
    # expiration overrides lifetime_in_seconds
    lifetime_in_seconds: pyd.PositiveInt = 30,
    expiration: DatetimeAsIntTimestamp | None = None,
    not_before: DatetimeAsIntTimestamp | None = None,
    add_nonce: bool = False,
) -> UcanPayload:
    """Construct the payload for a UCAN.

    Args:
        issuer (DidString): Issuer, the ID of who sent this.
        audience (DidString): Audience, the ID of who it's intended for.
        capabilities (list[Capability]): Attenuation, a list of resources and
            capabilities that the ucan grants.
        lifetime_in_seconds (pyd.PositiveInt, optional): Lifetime in seconds for which
            a UCAN should be valid for. This value is ignored when `expiration`
            is provided. Defaults to 30 seconds.
        expiration (DatetimeAsIntTimestamp | None, optional): Expiry, datetime of
            when the jwt is no longer valid. If provided, `lifetime_in_seconds`
            value will not be used. Defaults to None.
        not_before (DatetimeAsIntTimestamp | None, optional):  Not Before, datetime of
            when the jwt becomes valid. Defaults to None.
        add_nonce (bool, optional): Whether to add a nonce, a randomly generated string,
            used to ensure the uniqueness of the jwt. Defaults to False.

    Returns:
        UcanPayload: payload part of a UCAN.
    """
    now_ts = aware_utcnow()
    exp = expiration or (now_ts + dt.timedelta(seconds=lifetime_in_seconds))

    nonce = None
    if add_nonce:
        nonce = secrets.token_urlsafe()

    return UcanPayload(
        iss=issuer,
        aud=audience,
        exp=exp,
        att=capabilities,
        fct=None,
        prf=[],
        nbf=not_before,
        nnc=nonce,
    )


# Build token


@te.runtime_checkable
class TokenBuildFunc(te.Protocol):
    """Function prototype for the `.build` function."""

    async def __call__(  # noqa: D102, PLR0913
        self,
        issuer: DidableKey,
        audience: DidString,
        capabilities: list[Capability],
        *,
        # expiration overrides lifetime_in_seconds
        lifetime_in_seconds: pyd.PositiveInt = 30,
        expiration: DatetimeAsIntTimestamp | None = None,
        not_before: DatetimeAsIntTimestamp | None = None,
        add_nonce: bool = False,
    ) -> Ucan: ...


@validate_call
def build(plugins: Plugins) -> TokenBuildFunc:
    """Injects the plugins into the actual `build` implementation.

    Args:
        plugins (Plugins): Plugins to be injected.

    Returns:
        TokenBuildFunc: function with plugins injected.
    """

    @validate_call
    async def _build_inner(  # noqa: PLR0913
        issuer: DidableKey,
        audience: DidString,
        capabilities: list[Capability],
        *,
        # expiration overrides lifetime_in_seconds
        lifetime_in_seconds: pyd.PositiveInt = 30,
        expiration: DatetimeAsIntTimestamp | None = None,
        not_before: DatetimeAsIntTimestamp | None = None,
        add_nonce: bool = False,
    ) -> Ucan:
        """Create a UCAN, User Controlled Authorization Networks, JWT.

        Args:
            issuer (DidableKey): Issuer, the keypair of who sent this.
            audience (DidString): Audience, the ID of who it's intended for.
            capabilities (list[Capability]): Attenuation, a list of resources and
                capabilities that the ucan grants.
            lifetime_in_seconds (pyd.PositiveInt, optional): Lifetime in seconds for
                which a UCAN should be valid for. This value is ignored when
                `expiration` is provided. Defaults to 30 seconds.
            expiration (DatetimeAsIntTimestamp | None, optional): Expiry, datetime of
                when the jwt is no longer valid. If provided, `lifetime_in_seconds`
                value will not be used. Defaults to None.
            not_before (DatetimeAsIntTimestamp | None, optional):  Not Before, datetime
                of when the jwt becomes valid. Defaults to None.
            add_nonce (bool, optional): Whether to add a nonce, a randomly generated
                string, used to ensure the uniqueness of the jwt. Defaults to False.

        Returns:
            Ucan: a finalised UCAN.
        """
        payload = build_payload(
            issuer=issuer.did(),
            audience=audience,
            capabilities=capabilities,
            lifetime_in_seconds=lifetime_in_seconds,
            expiration=expiration,
            not_before=not_before,
            add_nonce=add_nonce,
        )

        return await sign_with_keypair(plugins)(payload, issuer)

    return _build_inner


# sign token


@te.runtime_checkable
class TokenSignFunc(te.Protocol):
    """Function prototype for the `.sign` function."""

    async def __call__(  # noqa: D102
        self, payload: UcanPayload, jwt_alg: str, sign_func: SignFuncCallback
    ) -> Ucan: ...


@validate_call
def sign(plugins: Plugins) -> TokenSignFunc:
    """Injects the plugins into the actual `sign` implementation.

    Args:
        plugins (Plugins): Plugins to be injected.

    Returns:
        TokenSignFunc: function with plugins injected.
    """

    @validate_call
    async def _sign_inner(
        payload: UcanPayload, jwt_alg: str, sign_func: SignFuncCallback
    ) -> Ucan:
        """Encloses a UCAN payload as to form a finalised UCAN.

        Args:
            payload (UcanPayload): UCAN payload to be signed.
            jwt_alg (str): Algorithm of the signing key.
            sign_func (SignFuncCallback): A callback function to sign the data.

        Returns:
            Ucan: a finalised UCAN.
        """
        header = UcanHeader(alg=jwt_alg, typ=TYPE, ucv=VERSION)

        if not await plugins.verify_issuer_alg(payload.iss, jwt_alg):
            msg = "The issuer's key type must match the given key type."
            raise ValueError(msg)

        encoded_header = header.encode()
        encoded_payload = payload.encode()

        signed_data = f"{encoded_header}.{encoded_payload}"
        to_sign = signed_data.encode("utf-8")
        signature_bytes = sign_func(to_sign)
        return Ucan(
            header=header,
            payload=payload,
            signed_data=signed_data,
            signature=Base64UrlEncoder.encode(signature_bytes),
        )

    return _sign_inner


# Sign with a keypair


@te.runtime_checkable
class TokenSignWithKeyPairFunc(te.Protocol):
    """Function prototype for the `.sign_with_keypair` function."""

    async def __call__(  # noqa: D102
        self, payload: UcanPayload, keypair: DidableKey
    ) -> Ucan: ...


@validate_call
def sign_with_keypair(plugins: Plugins) -> TokenSignWithKeyPairFunc:
    """Injects the plugins into the actual `sign_with_keypair` implementation.

    Args:
        plugins (Plugins): Plugins to be injected.

    Returns:
        TokenSignWithKeyPairFunc: function with plugins injected.
    """

    @validate_call
    async def _sign_with_keypair_inner(
        payload: UcanPayload, keypair: DidableKey
    ) -> Ucan:
        """`sign` with a `Keypair`.

        Args:
            payload (UcanPayload): UCAN payload to be signed.
            keypair (DidableKey): key pair to sign with.

        Returns:
            Ucan: a finalised UCAN.
        """
        return await sign(plugins)(
            payload, keypair.jwt_alg, lambda data: keypair.sign(data)
        )

    return _sign_with_keypair_inner


# Token parse


@te.runtime_checkable
class TokenParseFunc(te.Protocol):
    """Function prototype for the `.parse` function."""

    def __call__(self, encoded_ucan: str) -> Ucan: ...  # noqa: D102


@validate_call
def parse(plugins: Plugins) -> TokenParseFunc:  # noqa: ARG001
    """Injects the plugins into the actual `parse` implementation.

    Args:
        plugins (Plugins): Plugins to be injected.

    Returns:
        TokenParseFunc: function with plugins injected.
    """

    @validate_call
    def _parse_inner(encoded_ucan: str) -> Ucan:
        """Parse an encoded UCAN.

        Args:
            encoded_ucan (str): the encoded UCAN.

        Returns:
            Ucan: unverified and unvalidated UCAN.
        """
        return Ucan.decode(encoded_ucan)

    return _parse_inner


# Token Validate


@te.runtime_checkable
class TokenValidateFunc(te.Protocol):
    """Function prototype for the `.validate` function."""

    async def __call__(  # noqa: D102
        self,
        encoded_ucan: str,
        *,
        check_issuer: bool = True,
        check_signature: bool = True,
        check_is_expired: bool = True,
        check_is_too_early: bool = True,
    ) -> Ucan: ...


@validate_call
def validate(plugins: Plugins) -> TokenValidateFunc:
    """Injects the plugins into the actual `validate` implementation.

    Args:
        plugins (Plugins): Plugins to be injected.

    Returns:
        TokenValidateFunc: function with plugins injected.
    """

    @validate_call
    async def _validate_inner(
        encoded_ucan: str,
        *,
        check_issuer: bool = True,
        check_signature: bool = True,
        check_is_expired: bool = True,
        check_is_too_early: bool = True,
    ) -> Ucan:
        """Parse & Validate **one layer** of a UCAN.

        This doesn't validate attenutations and doesn't validate the whole UCAN chain.

        By default, this will check the issuer key type, signature and time bounds.

        Args:
            encoded_ucan (str): the JWT-encoded UCAN to validate
            check_issuer (bool, optional): Check whether the issuer's key type
                matches the UCAN header's `alg` property. Defaults to True.
            check_signature (bool, optional): Check whether the UCAN signature is valid.
                Defaults to True.
            check_is_expired (bool, optional): Check whether the UCAN token is expired.
                Defaults to True.
            check_is_too_early (bool, optional): Check whether the token is being
                used before its `nbf` value. Defaults to True.

        Raises:
            ValueError: Error if the UCAN is invalid

        Returns:
            Ucan: the parsed & validated UCAN (one layer)
        """
        parsed = parse(plugins)(encoded_ucan)

        if check_issuer and not await plugins.verify_issuer_alg(
            parsed.payload.iss, parsed.header.alg
        ):
            msg = (
                f"Invalid UCAN: {encoded_ucan}: Issuer key type does not "
                "match UCAN's `alg` property."
            )
            raise ValueError(msg)

        if check_signature:
            await plugins.verify_signature(
                parsed.payload.iss, parsed.signed_data_bytes, parsed.signature_bytes
            )

        if check_is_expired and is_expired(parsed):
            msg = f"Invalid UCAN: {encoded_ucan}: Expired."
            raise ValueError(msg)

        if check_is_too_early and is_too_early(parsed):
            msg = f"Invalid UCAN: {encoded_ucan}: Not active yet (too early)."
            raise ValueError(msg)

        return parsed

    return _validate_inner


# Validate Proofs


@te.runtime_checkable
class TokenValidateProofFunc(te.Protocol):
    """Function prototype for the `.validate_proofs` function."""

    def __call__(  # noqa: D102, PLR0913
        self,
        ucan: Ucan,
        *,
        check_addressing: bool = True,
        check_time_bounds_subset: bool = True,
        check_version_monotonic: bool = True,
        check_issuer: bool = True,
        check_signature: bool = True,
        check_is_expired: bool = True,
        check_is_too_early: bool = True,
    ) -> te.AsyncIterator[Ucan | Exception]: ...


@validate_call
def validate_proofs(plugins: Plugins) -> TokenValidateProofFunc:
    """Injects the plugins into the actual `validate_proofs` implementation.

    Args:
        plugins (Plugins): Plugins to be injected.

    Returns:
        TokenValidateProofFunc: function with plugins injected.
    """

    @validate_call
    async def _validate_proofs_inner(  # noqa: PLR0913
        ucan: Ucan,
        *,
        check_addressing: bool = True,
        check_time_bounds_subset: bool = True,
        check_version_monotonic: bool = True,
        check_issuer: bool = True,
        check_signature: bool = True,
        check_is_expired: bool = True,
        check_is_too_early: bool = True,
    ) -> te.AsyncIterator[Ucan | ProofError]:
        """Iterates over all proofs and parses & validates them at the same time.

        If there's an audience/issuer mismatch, the iterated item will
        contain an `ProofError`, otherwise the iterated out will contain a `Ucan`.

        Args:
            ucan (Ucan): The UCAN to validate.
            check_addressing (bool, optional): Whether to check if the ucan's
                issuer matches its proofs audiences. Defaults to True.
            check_time_bounds_subset (bool, optional): Whether to check if a ucan's
                time bounds are a subset of its proofs time bounds. Defaults to True.
            check_version_monotonic (bool, optional): Whether to check if a ucan's
                version is bigger or equal to its proofs version. Defaults to True.
            check_issuer (bool, optional): Check whether the issuer's key type
                matches the UCAN header's `alg` property. Defaults to True.
            check_signature (bool, optional): Check whether the UCAN signature is valid.
                Defaults to True.
            check_is_expired (bool, optional): Check whether the UCAN token is expired.
                Defaults to True.
            check_is_too_early (bool, optional): Check whether the token is being
                used before its `nbf` value. Defaults to True.

        Returns:
            te.AsyncIterator[Ucan | ProofError]: an async iterator of the given ucan's
                proofs parsed & validated, or an `ProofError` for each proof that
                couldn't be validated or parsed.
        """
        for prf in ucan.payload.prf:
            try:
                proof = await validate(plugins)(
                    prf,
                    check_issuer=check_issuer,
                    check_signature=check_signature,
                    check_is_expired=check_is_expired,
                    check_is_too_early=check_is_too_early,
                )
                if check_addressing and ucan.payload.iss != proof.payload.aud:
                    yield ProofError(
                        f"Invalid Proof: Issuer {ucan.payload.iss} doesn't match "
                        f"parent's audience {proof.payload.aud}"
                    )
                if (
                    check_time_bounds_subset
                    and proof.payload.nbf is not None
                    and ucan.payload.exp > proof.payload.nbf
                ):
                    yield ProofError(
                        f"Invalid Proof: 'Not before' ({proof.payload.nbf}) is "
                        f"after parent's expiration ({ucan.payload.exp})"
                    )

                if (
                    check_time_bounds_subset
                    and ucan.payload.nbf is not None
                    and ucan.payload.nbf > proof.payload.exp
                ):
                    yield ProofError(
                        f"Invalid Proof: Expiration ({proof.payload.exp}) is "
                        f"before parent's 'not before' ({ucan.payload.nbf})"
                    )

                if check_version_monotonic and ucan.header.ucv.lt(proof.header.ucv):
                    yield ProofError(
                        f"Invalid Proof: Version ({proof.header.ucv}) is higher "
                        f"than parent's version ({ucan.header.ucv})"
                    )

                yield proof

            except ProofError as e:  # noqa: PERF203
                yield e

            except Exception as e:
                yield ProofError(f"Error when trying to parse UCAN proof: {e}")

    return _validate_proofs_inner
