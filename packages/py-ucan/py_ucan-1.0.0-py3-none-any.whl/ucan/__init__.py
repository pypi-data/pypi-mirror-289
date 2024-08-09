"""ucan package root."""

from __future__ import annotations

import typing_extensions as te

import pydantic as pyd
import pydantic.dataclasses

from ucan.core import attenuation as attenuationlib
from ucan.core import token as tokenlib
from ucan.core import verify as verifylib
from ucan.core.capability import Ability, Capability, ResourcePointer
from ucan.core.plugins import Plugins
from ucan.core.types import Ucan, UcanHeader, UcanPayload
from ucan.core.verify import (
    RequiredCapability,
    Verification,
    VerifyResult,
    VerifyResultError,
    VerifyResultOk,
)
from ucan.default_plugins import ed25519_plugin, EdKeypair


__version__ = "1.0.0"


__all__ = (
    # attrs of this module
    "Plugins",
    "PluginInjectedAPI",
    "default_plugins",
    "injected_api",
    "build",
    "delegation_chains",
    "sign",
    "sign_with_keypair",
    "parse",
    "validate",
    "validate_proofs",
    "verify",
    "build_payload",
    # plugins
    "EdKeypair",
    "ed25519_plugin",
    # types
    "Ability",
    "Capability",
    "ResourcePointer",
    "Ucan",
    "UcanHeader",
    "UcanPayload",
    # verify types
    "RequiredCapability",
    "Verification",
    "VerifyResult",
    "VerifyResultError",
    "VerifyResultOk",
)


@pyd.dataclasses.dataclass(
    frozen=True,
    kw_only=True,
    config=pyd.ConfigDict(extra="forbid", frozen=True, arbitrary_types_allowed=True),
)
class PluginInjectedAPI:
    """Ucan API with plugins injected."""

    delegation_chains: attenuationlib.DelegationChainsFunc
    build: tokenlib.TokenBuildFunc
    sign: tokenlib.TokenSignFunc
    sign_with_keypair: tokenlib.TokenSignWithKeyPairFunc
    parse: tokenlib.TokenParseFunc
    validate: tokenlib.TokenValidateFunc
    validate_proofs: tokenlib.TokenValidateProofFunc
    verify: verifylib.VerifyTokenFunc

    @classmethod
    def from_plugins(cls, plugins: Plugins) -> te.Self:
        """Build `PluginInjectedAPI` from a `Plugins` object."""
        return cls(
            build=tokenlib.build(plugins),
            sign=tokenlib.sign(plugins),
            sign_with_keypair=tokenlib.sign_with_keypair(plugins),
            parse=tokenlib.parse(plugins),
            validate=tokenlib.validate(plugins),
            verify=verifylib.verify(plugins),
            validate_proofs=tokenlib.validate_proofs(plugins),
            delegation_chains=attenuationlib.delegation_chains(plugins),
        )


default_plugins = Plugins([ed25519_plugin])
injected_api = PluginInjectedAPI.from_plugins(default_plugins)

delegation_chains = injected_api.delegation_chains
build = injected_api.build
sign = injected_api.sign
sign_with_keypair = injected_api.sign_with_keypair
parse = injected_api.parse
validate = injected_api.validate
validate_proofs = injected_api.validate_proofs
verify = injected_api.verify

# extra generic functions
build_payload = tokenlib.build_payload
