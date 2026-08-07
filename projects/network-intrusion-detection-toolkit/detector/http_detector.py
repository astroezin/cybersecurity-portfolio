"""
HTTP threat detection module for the Network Intrusion Detection Toolkit.
"""

from datetime import datetime

from scapy.layers.http import HTTPRequest
from scapy.layers.inet import IP

from core.config import (
    DEFAULT_SEVERITY,
    MITRE_MAPPING,
)


SUSPICIOUS_USER_AGENTS = [
    "curl",
    "python-requests",
    "powershell",
    "wget",
    "sqlmap",
    "nikto",
    "nmap",
]


def detect_http_activity(
    packets
):
    """
    Detect suspicious HTTP activity.

    Looks for unusual HTTP user agents commonly
    associated with automation and reconnaissance tools.

    Args:
        packets (list): Scapy packets.

    Returns:
        list: Detection alerts.
    """

    alerts = []

    for packet in packets:

        if not packet.haslayer(
            HTTPRequest
        ):
            continue

        http = packet[
            HTTPRequest
        ]

        user_agent = ""

        if hasattr(
            http,
            "User_Agent"
        ):

            user_agent = http.User_Agent.decode(
                errors="ignore"
            )

        user_agent_lower = user_agent.lower()

        for suspicious in SUSPICIOUS_USER_AGENTS:

            if suspicious in user_agent_lower:

                source_ip = (
                    packet[IP].src
                    if packet.haslayer(IP)
                    else "Unknown"
                )

                destination_ip = (
                    packet[IP].dst
                    if packet.haslayer(IP)
                    else "Unknown"
                )

                alerts.append(
                    {
                        "alert_type":
                            "HTTP_ACTIVITY",

                        "severity":
                            DEFAULT_SEVERITY[
                                "HTTP_ACTIVITY"
                            ],

                        "description":
                            "Suspicious HTTP user agent detected",

                        "source_ip":
                            source_ip,

                        "destination_ip":
                            destination_ip,

                        "user_agent":
                            user_agent,

                        "timestamp":
                            datetime.fromtimestamp(
                                float(packet.time)
                            ).isoformat(),

                        "mitre":
                            MITRE_MAPPING[
                                "HTTP_ACTIVITY"
                            ],
                    }
                )

                break

    return alerts


def extract_http_hosts(
    packets
):
    """
    Extract HTTP host headers.

    Args:
        packets (list): Scapy packets.

    Returns:
        list: HTTP hosts.
    """

    hosts = []

    for packet in packets:

        if not packet.haslayer(
            HTTPRequest
        ):
            continue

        http = packet[
            HTTPRequest
        ]

        if hasattr(
            http,
            "Host"
        ):

            hosts.append(
                http.Host.decode(
                    errors="ignore"
                )
            )

    return hosts
