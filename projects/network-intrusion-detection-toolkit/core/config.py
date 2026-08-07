"""
Configuration settings for the Network Intrusion Detection Toolkit.
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


LOG_DIR = BASE_DIR / "logs"

REPORT_DIR = BASE_DIR / "reports"

SAMPLE_DIR = BASE_DIR / "samples"


LOG_FILE = LOG_DIR / "nids.log"


DEFAULT_SEVERITY = {
    "SYN_SCAN": "HIGH",
    "PORT_SCAN": "MEDIUM",
    "DNS_ACTIVITY": "MEDIUM",
    "ARP_SPOOFING": "CRITICAL",
    "HTTP_ACTIVITY": "LOW",
}


MITRE_MAPPING = {
    "SYN_SCAN": [
        "T1046 - Network Service Scanning"
    ],

    "PORT_SCAN": [
        "T1046 - Network Service Scanning"
    ],

    "DNS_ACTIVITY": [
        "T1071.004 - DNS"
    ],

    "ARP_SPOOFING": [
        "T1557.002 - ARP Cache Poisoning"
    ],

    "HTTP_ACTIVITY": [
        "T1071.001 - Web Protocols"
    ],
}


SUPPORTED_PROTOCOLS = [
    "TCP",
    "UDP",
    "ICMP",
    "DNS",
    "HTTP",
    "ARP",
]


def create_directories():
    """
    Create required project directories.
    """

    LOG_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    REPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    SAMPLE_DIR.mkdir(
        parents=True,
        exist_ok=True
    )
