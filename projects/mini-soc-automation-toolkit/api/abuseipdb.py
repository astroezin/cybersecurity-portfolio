"""
AbuseIPDB API integration module.

Provides IP reputation intelligence.
"""

import requests

from core.config import Config


BASE_URL = "https://api.abuseipdb.com/api/v2"


def _headers():
    """
    Build AbuseIPDB headers.
    """

    return {
        "Key": Config.ABUSEIPDB_API_KEY,
        "Accept": "application/json"
    }


def lookup_ip(ip_address):
    """
    Lookup IP reputation.
    """

    endpoint = f"{BASE_URL}/check"

    params = {
        "ipAddress": ip_address,
        "maxAgeInDays": 90
    }

    try:
        response = requests.get(
            endpoint,
            headers=_headers(),
            params=params,
            timeout=10
        )

        if response.status_code != 200:
            return {
                "error": (
                    f"AbuseIPDB API error "
                    f"{response.status_code}"
                )
            }

        return response.json()

    except requests.RequestException as error:
        return {
            "error": str(error)
        }


def analyze_result(data):
    """
    Extract useful AbuseIPDB information.
    """

    if "error" in data:
        return data

    result = (
        data
        .get("data", {})
    )

    return {
        "country": result.get(
            "countryCode",
            "N/A"
        ),

        "isp": result.get(
            "isp",
            "N/A"
        ),

        "domain": result.get(
            "domain",
            "N/A"
        ),

        "abuse_score": result.get(
            "abuseConfidenceScore",
            0
        ),

        "total_reports": result.get(
            "totalReports",
            0
        ),

        "distinct_users": result.get(
            "numDistinctUsers",
            0
        )
    }
