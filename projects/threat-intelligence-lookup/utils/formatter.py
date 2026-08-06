"""
Formatting utilities for Threat Intelligence Lookup.
"""


def format_virustotal_ip(data):
    """
    Format a VirusTotal IP lookup response.

    Args:
        data (dict): VirusTotal JSON response.

    Returns:
        str: Human-readable report.
    """
    attributes = data["data"]["attributes"]

    stats = attributes.get("last_analysis_stats", {})

    return f"""
=========================================
VirusTotal IP Intelligence
=========================================

IP Address : {data["data"]["id"]}

Country    : {attributes.get("country", "N/A")}
ASN        : {attributes.get("asn", "N/A")}
Owner      : {attributes.get("as_owner", "N/A")}

----------- Detection Statistics --------

Malicious  : {stats.get("malicious", 0)}
Suspicious : {stats.get("suspicious", 0)}
Harmless   : {stats.get("harmless", 0)}
Undetected : {stats.get("undetected", 0)}
Timeout    : {stats.get("timeout", 0)}

=========================================
""".strip()
def format_abuseipdb_ip(data):
    """
    Format an AbuseIPDB response.
    """
    ip = data["data"]

    return f"""
=========================================
AbuseIPDB Intelligence
=========================================

IP Address : {ip.get("ipAddress")}

Country    : {ip.get("countryCode")}
ISP        : {ip.get("isp")}
Domain     : {ip.get("domain")}
Usage Type : {ip.get("usageType")}

----------- Reputation -----------

Abuse Score : {ip.get("abuseConfidenceScore")}%
Reports     : {ip.get("totalReports")}
Distinct Users : {ip.get("numDistinctUsers")}

=========================================
""".strip()
