"""
File monitoring module for Endpoint Detection & Response Simulator.
"""

from detection.behavior_rules import (
    is_suspicious_extension,
)


def analyze_files(
    file_events
):
    """
    Analyze file creation events.

    Args:
        file_events (list): File activity events.

    Returns:
        list: Detection alerts.
    """

    alerts = []

    for event in file_events:

        filename = event.get(
            "filename",
            ""
        )

        path = event.get(
            "path",
            ""
        )

        user = event.get(
            "user",
            "unknown"
        )


        if is_suspicious_extension(
            filename
        ):

            alerts.append(
                {
                    "type":
                        "SUSPICIOUS_FILE",

                    "severity":
                        "MEDIUM",

                    "description":
                        (
                            "Suspicious executable file "
                            f"created: {filename}"
                        ),

                    "file":
                        filename,

                    "path":
                        path,

                    "user":
                        user,

                    "mitre":
                        [
                            "T1204 - User Execution"
                        ],
                }
            )


    return alerts
