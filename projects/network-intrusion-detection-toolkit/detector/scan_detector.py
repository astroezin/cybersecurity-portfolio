"""
Port scan and network reconnaissance detection module.
"""

from collections import defaultdict
from datetime import datetime

from scapy.layers.inet import IP, TCP

from core.config import (
    DEFAULT_SEVERITY,
    MITRE_MAPPING,
)


def detect_syn_scan(
    packets,
    threshold=10
):
    """
    Detect possible SYN port scans.

    A SYN scan is identified when a single source IP
    sends SYN packets to many destination ports.

    Args:
        packets (list): Scapy packets.
        threshold (int): Minimum ports contacted.

    Returns:
        list: Detection alerts.
    """

    connections = defaultdict(set)
    timestamps = {}

    for packet in packets:

        if not packet.haslayer(IP):
            continue

        if not packet.haslayer(TCP):
            continue

        tcp_layer = packet[TCP]

        if tcp_layer.flags == "S":

            source = packet[IP].src
            destination = packet[IP].dst

            connections[
                source
            ].add(
                tcp_layer.dport
            )

            timestamps[source] = (
                datetime.fromtimestamp(
                    float(packet.time)
                ).isoformat()
            )

    alerts = []

    for source, ports in connections.items():

        if len(ports) >= threshold:

            alerts.append(
                {
                    "alert_type": "SYN_SCAN",
                    "severity": DEFAULT_SEVERITY[
                        "SYN_SCAN"
                    ],
                    "description":
                        "Possible SYN port scan detected",
                    "source_ip": source,
                    "ports_scanned": sorted(
                        list(ports)
                    ),
                    "timestamp": timestamps.get(
                        source
                    ),
                    "mitre": MITRE_MAPPING[
                        "SYN_SCAN"
                    ],
                }
            )

    return alerts


def detect_port_scan(
    packets,
    threshold=15
):
    """
    Detect broad port scanning activity.

    Args:
        packets (list): Scapy packets.
        threshold (int): Number of unique ports.

    Returns:
        list: Detection alerts.
    """

    source_ports = defaultdict(set)

    for packet in packets:

        if not packet.haslayer(IP):
            continue

        if not packet.haslayer(TCP):
            continue

        source_ip = packet[IP].src

        source_ports[source_ip].add(
            packet[TCP].dport
        )

    alerts = []

    for source_ip, ports in source_ports.items():

        if len(ports) >= threshold:

            alerts.append(
                {
                    "alert_type": "PORT_SCAN",
                    "severity": DEFAULT_SEVERITY[
                        "PORT_SCAN"
                    ],
                    "description":
                        "Possible port scan activity detected",
                    "source_ip": source_ip,
                    "ports": sorted(
                        list(ports)
                    ),
                    "mitre": MITRE_MAPPING[
                        "PORT_SCAN"
                    ],
                }
            )

    return alerts
