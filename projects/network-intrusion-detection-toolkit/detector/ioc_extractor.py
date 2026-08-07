"""
IOC extraction module for the Network Intrusion Detection Toolkit.
"""

import re

from scapy.layers.dns import DNSQR
from scapy.layers.http import HTTPRequest
from scapy.layers.inet import IP


IP_PATTERN = re.compile(
    r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
)

DOMAIN_PATTERN = re.compile(
    r"\b[a-zA-Z0-9.-]+\.(?:com|net|org|io|gov|edu|co|info)\b"
)


def extract_ip_addresses(
    packets
):
    """
    Extract IP addresses from packets.

    Args:
        packets (list): Scapy packets.

    Returns:
        list: Unique IP addresses.
    """

    ips = set()

    for packet in packets:

        if packet.haslayer(IP):

            ips.add(
                packet[IP].src
            )

            ips.add(
                packet[IP].dst
            )

    return sorted(
        list(ips)
    )


def extract_domains(
    packets
):
    """
    Extract domains from DNS and HTTP traffic.

    Args:
        packets (list): Scapy packets.

    Returns:
        list: Unique domains.
    """

    domains = set()

    for packet in packets:

        if packet.haslayer(
            DNSQR
        ):

            domain = packet[
                DNSQR
            ].qname.decode(
                errors="ignore"
            )

            domains.add(
                domain.rstrip(".")
            )

        if packet.haslayer(
            HTTPRequest
        ):

            http = packet[
                HTTPRequest
            ]

            if hasattr(
                http,
                "Host"
            ):

                host = http.Host.decode(
                    errors="ignore"
                )

                domains.add(
                    host
                )

    return sorted(
        list(domains)
    )


def extract_iocs(
    packets
):
    """
    Extract all network indicators.

    Args:
        packets (list): Scapy packets.

    Returns:
        dict: IOC information.
    """

    return {
        "ip_addresses":
            extract_ip_addresses(
                packets
            ),

        "domains":
            extract_domains(
                packets
            ),
    }
