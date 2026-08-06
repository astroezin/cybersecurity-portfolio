"""
VirusTotal API integration module.

Supports:
- IP reputation lookup
- Domain reputation lookup
- File hash lookup
"""

import requests

from core.config import Config


BASE_URL = "https://www.virustotal.com/api/v3"


def _headers():
    """
    Build API headers.
    """

    return {
        "x-apikey": Config.VIRUSTOTAL_API_KEY
    }


def _request(endpoint):
    """
    Send GET request to VirusTotal.
    """

    try:
        response = requests.get(
            f"{BASE_URL}/{endpoint}",
            headers=_headers(),
            timeout=10
        )

        if response.status_code != 200:
            return {
                "error": (
                    f"VirusTotal API error "
                    f"{response.status_code}"
                )
            }

        return response.json()

    except requests.RequestException as error:
        return {
            "error": str(error)
        }


def lookup_ip(ip_address):
    """
    Lookup IPv4 address reputation.
    """

    return _request(
        f"ip_addresses/{ip_address}"
    )


def lookup_domain(domain):
    """
    Lookup domain reputation.
    """

    return _request(
        f"domains/{domain}"
    )


def lookup_hash(file_hash):
    """
    Lookup file hash reputation.
    """

    return _request(
        f"files/{file_hash}"
    )


def analyze_result(data):
    """
    Extract useful VirusTotal information.
    """

    if "error" in data:
        return data

    attributes = (
        data
        .get("data", {})
        .get("attributes", {})
    )

    stats = attributes.get(
        "last_analysis_stats",
        {}
    )

    return {
        "country": attributes.get(
            "country",
            "N/A"
        ),

        "owner": attributes.get(
            "as_owner",
            "N/A"
        ),

        "malicious": stats.get(
            "malicious",
            0
        ),

        "suspicious": stats.get(
            "suspicious",
            0
        ),

        "harmless": stats.get(
            "harmless",
            0
        ),

        "undetected": stats.get(
            "undetected",
            0
        )
    }
