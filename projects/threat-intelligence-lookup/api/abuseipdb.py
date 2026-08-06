"""
AbuseIPDB API client.
"""

import requests

from utils.config import ABUSEIPDB_API_KEY


BASE_URL = "https://api.abuseipdb.com/api/v2/check"


class AbuseIPDBError(Exception):
    """Raised when an AbuseIPDB request fails."""


def lookup_ip(ip_address):
    """
    Query AbuseIPDB for an IPv4 address.

    Args:
        ip_address (str): IPv4 address.

    Returns:
        dict: Parsed JSON response.
    """
    headers = {
        "Key": ABUSEIPDB_API_KEY,
        "Accept": "application/json",
    }

    params = {
        "ipAddress": ip_address,
        "maxAgeInDays": 90,
        "verbose": True,
    }

    try:
        response = requests.get(
            BASE_URL,
            headers=headers,
            params=params,
            timeout=15,
        )

        if response.status_code != 200:
            raise AbuseIPDBError(
                f"HTTP {response.status_code}: {response.text}"
            )

        return response.json()

    except requests.RequestException as exc:
        raise AbuseIPDBError(
            f"Connection error: {exc}"
        ) from exc
