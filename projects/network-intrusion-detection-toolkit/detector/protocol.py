"""
Protocol analysis module for the Network Intrusion Detection Toolkit.
"""

from collections import Counter

from scapy.layers.inet import ICMP, IP, TCP, UDP
from scapy.layers.l2 import ARP
from scapy.layers.dns import DNS


def identify_protocol(packet):
    """
    Identify the primary protocol for a packet.

    Args:
        packet: Scapy packet.

    Returns:
        str: Protocol name.
    """

    if packet.haslayer(ARP):
        return "ARP"

    if packet.haslayer(DNS):
        return "DNS"

    if packet.haslayer(TCP):
        return "TCP"

    if packet.haslayer(UDP):
        return "UDP"

    if packet.haslayer(ICMP):
        return "ICMP"

    if packet.haslayer(IP):
        return "IP"

    return "OTHER"


def protocol_distribution(packets):
    """
    Count packets by protocol.

    Args:
        packets (list): Scapy packets.

    Returns:
        dict
    """

    counter = Counter()

    for packet in packets:
        counter.update(
            [identify_protocol(packet)]
        )

    return dict(counter)


def protocol_percentages(packets):
    """
    Calculate protocol percentages.

    Args:
        packets (list): Scapy packets.

    Returns:
        dict
    """

    distribution = protocol_distribution(packets)

    total = sum(distribution.values())

    if total == 0:
        return {}

    return {
        protocol: round(
            (count / total) * 100,
            2
        )
        for protocol, count in distribution.items()
    }


def extract_ip_pairs(packets):
    """
    Extract source/destination IP pairs.

    Args:
        packets (list): Scapy packets.

    Returns:
        list
    """

    pairs = []

    for packet in packets:

        if not packet.haslayer(IP):
            continue

        pairs.append(
            {
                "source": packet[IP].src,
                "destination": packet[IP].dst,
                "protocol": identify_protocol(packet),
            }
        )

    return pairs
