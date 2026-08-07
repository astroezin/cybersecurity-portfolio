"""
Timeline generation module for the Network Intrusion Detection Toolkit.
"""

from datetime import datetime


def create_timeline(
    packets
):
    """
    Generate a chronological packet timeline.

    Args:
        packets (list): Scapy packets.

    Returns:
        list: Timeline events.
    """

    timeline = []

    for index, packet in enumerate(
        packets,
        start=1
    ):

        timestamp = datetime.fromtimestamp(
            float(packet.time)
        ).isoformat()

        timeline.append(
            {
                "event_id": index,
                "timestamp": timestamp,
                "packet_length": len(packet),
            }
        )

    return sorted(
        timeline,
        key=lambda item: item["timestamp"]
    )


def summarize_timeline(
    timeline
):
    """
    Create timeline summary.

    Args:
        timeline (list): Timeline events.

    Returns:
        dict
    """

    if not timeline:

        return {
            "first_event": None,
            "last_event": None,
            "total_events": 0,
        }

    return {
        "first_event":
            timeline[0]["timestamp"],

        "last_event":
            timeline[-1]["timestamp"],

        "total_events":
            len(timeline),
    }
