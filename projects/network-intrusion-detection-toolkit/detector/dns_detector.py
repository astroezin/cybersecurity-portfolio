"""
DNS threat detection module for the Network Intrusion Detection Toolkit.
"""

from collections import defaultdict
from datetime import datetime

from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP

from core.config import (
    DEFAULT_SEVERITY,
    MITRE_MAPPING,
)


def detect_dns_activity(
    packets,
    threshold=20
):
    """
    Detect excessive DNS query activity.

    High DNS request volume from a single host
    can indicate scanning, malware communication,
    or DNS tunneling attempts.

    Args:
        packets (list): Scapy packets.
        threshold (int): DNS query count threshold.

    Returns:
        list: Detection alerts.
    """

    dns_requests = defaultdict(list)

    for packet in packets:

        if not packet.haslayer(DNS):
            continue

        if not packet.haslayer(DNSQR):
            continue

        if packet[DNS].qr != 0:
            continue

        source_ip = "Unknown"

        if packet.haslayer(IP):
            source_ip = packet[IP].src

        query = packet[DNSQR].qname.decode(
            errors="ignore"
        )

        timestamp = datetime.fromtimestamp(
            float(packet.time)
        ).isoformat()

        dns_requests[source_ip].append(
            {
                "domain": query,
                "timestamp": timestamp,
            }
        )

    alerts = []

    for source_ip, requests in dns_requests.items():

        if len(requests) >= threshold:

            alerts.append(
                {
                    "alert_type": "DNS_ACTIVITY",
                    "severity": DEFAULT_SEVERITY[
                        "DNS_ACTIVITY"
                    ],
                    "description":
                        "High volume DNS queries detected",
                    "source_ip": source_ip,
                    "query_count": len(
                        requests
                    ),
                    "domains": [
                        item["domain"]
                        for item in requests[:10]
                    ],
                    "timestamp": requests[0][
                        "timestamp"
                    ],
                    "mitre": MITRE_MAPPING[
                        "DNS_ACTIVITY"
                    ],
                }
            )

    return alerts


def extract_dns_queries(
    packets
):
    """
    Extract DNS queries from packets.

    Args:
        packets (list): Scapy packets.

    Returns:
        list: DNS query information.
    """

    queries = []

    for packet in packets:

        if not packet.haslayer(DNSQR):
            continue

        query = packet[
            DNSQR
        ].qname.decode(
            errors="ignore"
        )

        queries.append(
            {
                "domain": query,
                "source": (
                    packet[IP].src
                    if packet.haslayer(IP)
                    else "Unknown"
                ),
            }
        )

    return queries
