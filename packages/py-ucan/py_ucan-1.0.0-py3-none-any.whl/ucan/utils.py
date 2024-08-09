from __future__ import annotations

import datetime as dt
import typing as t

import base58

from ucan.constants import PREFIX_DID_BASE58


# datetime helpers


def aware_utcnow() -> dt.datetime:
    """Construct a timezone (UTC) aware datetime."""
    return dt.datetime.now(dt.timezone.utc)


def aware_utcfromtimestamp(timestamp: float) -> dt.datetime:
    """Construct a timezone (UTC) aware datetime from a POSIX timestamp."""
    return dt.datetime.fromtimestamp(timestamp, dt.timezone.utc)


def naive_utcnow() -> dt.datetime:
    """Construct a non-timezone aware datetime in UTC."""
    return aware_utcnow().replace(tzinfo=None)


def naive_utcfromtimestamp(timestamp: float) -> dt.datetime:
    """Construct a non-timezone aware datetime in UTC from a POSIX timestamp."""
    return aware_utcfromtimestamp(timestamp).replace(tzinfo=None)


def isoformat(o: dt.date | dt.time) -> str:
    """Return the date formatted according to ISO."""
    return o.isoformat()


# general helpers


def has_prefix(data: t.AnyStr, prefix: t.AnyStr) -> bool:
    """Determines if a string like value startswith a given indeterminate length-prefix.

    Args:
        data (t.AnyStr): data to check.
        prefix (t.AnyStr): expected indeterminate length-prefix.

    Returns:
        bool: whether `data` startswith `prefix`.
    """
    return data.startswith(prefix)


def parse_prefixed_str(data: str, prefix: str) -> str:
    """Get the substring from `data` after the given `prefix`.

    Args:
        data (str): string data.
        prefix (str): prefix to look for.

    Raises:
        ValueError: Length of data is less than that of prefix
        ValueError: `data` value does not contain the prefix `prefix`

    Returns:
        str: substring after the prefix.
    """
    if len(data) < len(prefix):
        msg = "Length of data is less than that of prefix"
        raise ValueError(msg)

    if not has_prefix(data, prefix):
        msg = "`data` value does not contain the prefix `prefix`"
        raise ValueError(msg)

    return data[len(prefix) :]


# cryptography helpers


def is_did(data: str) -> bool:
    """Check if a value is a valid DID.

    Args:
        data (str): value to validate.

    Returns:
        bool: Whether the value is a valid DID.
    """
    return data.startswith(PREFIX_DID_BASE58)


def validate_is_did(data: str) -> str:
    """Validate if a value is a valid DID.

    Args:
        data (str): value to validate.

    Raises:
        ValueError: Invalid DID string.

    Returns:
        str: a valid DID string.
    """
    if not is_did(data):
        msg = f"Expected a DID strings, but got {data}"
        raise ValueError(msg)

    return data


def parse_did_prefixed_bytes(did: str) -> bytes:
    """Parse the prefixed bytes from a DID.

    Args:
        did (str): DID to extract from.

    Raises:
        ValueError: Not a valid DID

    Returns:
        bytes: base58 representation of the data after the DID prefix.
    """
    if not is_did(did):
        msg = f"Not a valid base58 formatted did:key: {did}"
        raise ValueError(msg)

    did_without_prefix = parse_prefixed_str(did, PREFIX_DID_BASE58)
    return base58.b58decode(did_without_prefix)


def did_from_key_bytes(public_key_bytes: bytes, prefix: bytes) -> str:
    """Build DID from the given public key and prefix.

    Args:
        public_key_bytes (bytes): bytes representation of a public key.
        prefix (bytes): prefix for the DID.

    Returns:
        str: a finalized DID.
    """
    data_bytes = prefix + public_key_bytes
    base58_key = base58.b58encode(data_bytes).decode()
    return PREFIX_DID_BASE58 + base58_key


def did_to_key_bytes(did: str, expected_prefix: bytes) -> bytes:
    """Extract the public key bytes from the given DID and the expected prefix.

    Args:
        did (str): DID value.
        expected_prefix (bytes): expected prefix of the key.

    Raises:
        ValueError: Prefix not present.

    Returns:
        bytes: bytes representation of a public key.
    """
    data_bytes = parse_did_prefixed_bytes(did)

    if not has_prefix(data_bytes, expected_prefix):
        msg = f"Expected prefix: {expected_prefix.decode()}"
        raise ValueError(msg)

    return data_bytes[len(expected_prefix) :]
