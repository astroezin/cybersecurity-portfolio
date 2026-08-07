"""
Statistics module for the Network Intrusion Detection Toolkit.
"""

from collections import Counter


def calculate_statistics(
    packets
):
    """
    Calculate network traffic statistics.

    Args:
        packets (list): Scapy packets.

    Returns:
        dict: Traffic statistics.
    """

    protocol_counter = Counter()

    source_counter = Counter()

    destination_counter = Counter()

    packet_sizes = []

    for packet in packets:

        packet_sizes.append(
            len(packet)
        )

        if packet.haslayer("IP"):

            source_counter.update(
                [packet["IP"].src]
            )

            destination_counter.update(
                [packet["IP"].dst]
            )

        protocol = packet.__class__.__name__

        protocol_counter.update(
            [protocol]
        )

    return {
        "total_packets":
            len(packets),

        "protocols":
            dict(protocol_counter),

        "top_sources":
            dict(
                source_counter.most_common(10)
            ),

        "top_destinations":
            dict(
                destination_counter.most_common(10)
            ),

        "packet_size": {
            "minimum":
                min(packet_sizes)
                if packet_sizes
                else 0,

            "maximum":
                max(packet_sizes)
                if packet_sizes
                else 0,

            "average":
                round(
                    sum(packet_sizes)
                    / len(packet_sizes),
                    2
                )
                if packet_sizes
                else 0,
        },
    }


def count_alerts(
    alerts
):
    """
    Count alerts by severity.

    Args:
        alerts (list): Detection alerts.

    Returns:
        dict
    """

    severity_counter = Counter()

    for alert in alerts:

        severity_counter.update(
            [
                alert.get(
                    "severity",
                    "UNKNOWN"
                )
            ]
        )

    return dict(
        severity_counter
    )
