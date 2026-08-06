"""
VirusTotal API client.
"""

import requests

from utils.config import VIRUSTOTAL_API_KEY


BASE_URL = "https://www.virustotal.com/api/v3"


class VirusTotalError(Exception):
    """Raised when a VirusTotal request fails."""


def _headers():
    """Return the HTTP headers for VirusTotal requests."""
    return {
        "accept": "application/json",
        "x-apikey": VIRUSTOTAL_API_KEY,
    }


def lookup_ip(ip_address):
    """
    Look up an IPv4 address using the VirusTotal API.

    Args:
        ip_address (str): IPv4 address.

    Returns:
        dict: Parsed JSON response.

    Raises:
        VirusTotalError: If the request fails.
    """
    url = f"{BASE_URL}/ip_addresses/{ip_address}"

    try:
        response = requests.get(
            url,
            headers=_headers(),
            timeout=15,
        )

        if response.status_code != 200:
            raise VirusTotalError(
                f"VirusTotal returned HTTP {response.status_code}: "
                f"{response.text}"
            )

        return response.json()

    except requests.RequestException as exc:
        raise VirusTotalError(f"Connection error: {exc}") from exc
