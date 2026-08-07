"""
ARP attack detection module for the Network Intrusion Detection Toolkit.
"""

from collections import defaultdict
from datetime import datetime

from scapy.layers.l2 import ARP

from core.config import (
    DEFAULT_SEVERITY,
    MITRE_MAPPING,
)


def detect_arp_spoofing(
    packets
):
    """
    Detect possible ARP spoofing activity.

    ARP spoofing is identified when multiple MAC
    addresses claim ownership of the same IP address.

    Args:
        packets (list): Scapy packets.

    Returns:
        list: Detection alerts.
    """

    ip_mac_mapping = defaultdict(set)

    timestamps = {}

    for packet in packets:

        if not packet.haslayer(ARP):
            continue

        arp = packet[ARP]

        ip_address = arp.psrc
        mac_address = arp.hwsrc

        ip_mac_mapping[
            ip_address
        ].add(
            mac_address
        )

        timestamps[
            ip_address
        ] = datetime.fromtimestamp(
            float(packet.time)
        ).isoformat()

    alerts = []

    for ip_address, mac_addresses in ip_mac_mapping.items():

        if len(mac_addresses) > 1:

            alerts.append(
                {
                    "alert_type": "ARP_SPOOFING",
                    "severity": DEFAULT_SEVERITY[
                        "ARP_SPOOFING"
                    ],
                    "description":
                        "Possible ARP spoofing attack detected",
                    "target_ip": ip_address,
                    "mac_addresses": sorted(
                        list(mac_addresses)
                    ),
                    "timestamp": timestamps.get(
                        ip_address
                    ),
                    "mitre": MITRE_MAPPING[
                        "ARP_SPOOFING"
                    ],
                }
            )

    return alerts


def extract_arp_table(
    packets
):
    """
    Build an ARP table from packets.

    Args:
        packets (list): Scapy packets.

    Returns:
        dict: IP to MAC mapping.
    """

    arp_table = {}

    for packet in packets:

        if not packet.haslayer(ARP):
            continue

        arp = packet[ARP]

        arp_table[
            arp.psrc
        ] = arp.hwsrc

    return arp_table
