"""
Network behavior detection module for Endpoint Detection & Response Simulator.
"""

from detection.behavior_rules import (
    is_suspicious_port,
)


def analyze_network_events(
    network_events
):
    """
    Analyze endpoint network activity.

    Args:
        network_events (list): Network connections.

    Returns:
        list: Detection alerts.
    """

    alerts = []

    for event in network_events:

        destination = event.get(
            "destination",
            ""
        )

        port = event.get(
            "port",
            0
        )

        process = event.get(
            "process",
            ""
        )


        if is_suspicious_port(
            port
        ):

            alerts.append(
                {
                    "type":
                        "SUSPICIOUS_NETWORK_CONNECTION",

                    "severity":
                        "HIGH",

                    "description":
                        (
                            "Suspicious outbound "
                            "connection detected"
                        ),

                    "destination":
                        destination,

                    "port":
                        port,

                    "process":
                        process,

                    "mitre":
                        [
                            "T1071 - Application "
                            "Layer Protocol"
                        ],
                }
            )


    return alerts
