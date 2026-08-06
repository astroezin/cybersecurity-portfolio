"""
Input validation utilities for Threat Intelligence Lookup.
"""

import ipaddress
import re
from urllib.parse import urlparse


MD5_PATTERN = re.compile(r"^[A-Fa-f0-9]{32}$")
SHA1_PATTERN = re.compile(r"^[A-Fa-f0-9]{40}$")
SHA256_PATTERN = re.compile(r"^[A-Fa-f0-9]{64}$")
DOMAIN_PATTERN = re.compile(
    r"^(?!-)(?:[A-Za-z0-9-]{1,63}\.)+[A-Za-z]{2,63}$"
)


def is_ipv4(value):
    """Return True if value is a valid IPv4 address."""
    try:
        ip = ipaddress.ip_address(value)
        return ip.version == 4
    except ValueError:
        return False


def is_url(value):
    """Return True if value is a valid HTTP or HTTPS URL."""
    try:
        parsed = urlparse(value)
        return (
            parsed.scheme in ("http", "https")
            and bool(parsed.netloc)
        )
    except Exception:
        return False


def is_domain(value):
    """Return True if value is a valid domain."""
    return bool(DOMAIN_PATTERN.fullmatch(value))


def detect_hash(value):
    """Return the hash type or None."""
    if MD5_PATTERN.fullmatch(value):
        return "md5"

    if SHA1_PATTERN.fullmatch(value):
        return "sha1"

    if SHA256_PATTERN.fullmatch(value):
        return "sha256"

    return None


def detect_ioc_type(value):
    """
    Detect the IOC type.

    Returns:
        ip
        domain
        url
        md5
        sha1
        sha256
        None
    """

    if is_ipv4(value):
        return "ip"

    if is_url(value):
        return "url"

    if is_domain(value):
        return "domain"

    hash_type = detect_hash(value)
    if hash_type:
        return hash_type

    return None

