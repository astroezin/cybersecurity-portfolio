"""
IOC validation module.

Detects different Indicator of Compromise (IOC) types:
- IPv4 addresses
- Domains
- URLs
- MD5 hashes
- SHA1 hashes
- SHA256 hashes
"""

import hashlib
import ipaddress
import re
from urllib.parse import urlparse


def is_ipv4(value):
    """
    Check if value is a valid IPv4 address.
    """

    try:
        ipaddress.IPv4Address(value)
        return True

    except ValueError:
        return False


def is_url(value):
    """
    Check if value is a valid URL.
    """

    try:
        parsed = urlparse(value)

        return parsed.scheme in (
            "http",
            "https"
        ) and bool(parsed.netloc)

    except Exception:
        return False


def is_domain(value):
    """
    Check if value looks like a domain.
    """

    pattern = (
        r"^(?!-)"
        r"[A-Za-z0-9-]{1,63}"
        r"(\.[A-Za-z]{2,})+$"
    )

    return bool(
        re.match(pattern, value)
    )


def get_hash_type(value):
    """
    Detect hash algorithm based on length.
    """

    hash_lengths = {
        32: "MD5",
        40: "SHA1",
        64: "SHA256"
    }

    return hash_lengths.get(
        len(value)
    )


def validate_ioc(value):
    """
    Identify IOC type.

    Returns dictionary containing:
    - indicator
    - type
    - valid status
    """

    value = value.strip()

    if is_ipv4(value):
        return {
            "indicator": value,
            "type": "IPv4",
            "valid": True
        }

    if is_url(value):
        return {
            "indicator": value,
            "type": "URL",
            "valid": True
        }

    hash_type = get_hash_type(value)

    if hash_type:
        return {
            "indicator": value,
            "type": hash_type,
            "valid": True
        }

    if is_domain(value):
        return {
            "indicator": value,
            "type": "Domain",
            "valid": True
        }

    return {
        "indicator": value,
        "type": "Unknown",
        "valid": False
    }
