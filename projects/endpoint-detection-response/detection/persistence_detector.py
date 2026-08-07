"""
Persistence detection module for Endpoint Detection & Response Simulator.
"""

from detection.behavior_rules import (
    is_suspicious_extension,
)


def analyze_persistence(
    startup_entries
):
    """
    Detect suspicious persistence mechanisms.

    Args:
        startup_entries (list): Startup items.

    Returns:
        list: Detection alerts.
    """

    alerts = []

    for entry in startup_entries:

        name = entry.get(
            "name",
            ""
        )

        location = entry.get(
            "location",
            ""
        )

        command = entry.get(
            "command",
            ""
        )


        if is_suspicious_extension(
            command
        ):

            alerts.append(
                {
                    "type":
                        "PERSISTENCE_DETECTED",

                    "severity":
                        "HIGH",

                    "description":
                        (
                            "Suspicious startup "
                            f"entry detected: {name}"
                        ),

                    "location":
                        location,

                    "command":
                        command,

                    "mitre":
                        [
                            "T1547 - Boot or Logon "
                            "Autostart Execution"
                        ],
                }
            )


    return alerts
