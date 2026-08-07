"""
Process monitoring module for Endpoint Detection & Response Simulator.
"""

from detection.behavior_rules import (
    is_suspicious_process,
    contains_suspicious_command,
)


def analyze_processes(
    processes
):
    """
    Analyze running processes.

    Args:
        processes (list): Process events.

    Returns:
        list: Detection alerts.
    """

    alerts = []

    for process in processes:

        name = process.get(
            "name",
            ""
        )

        command = process.get(
            "command",
            ""
        )

        if is_suspicious_process(
            name
        ):

            alerts.append(
                {
                    "type":
                        "SUSPICIOUS_PROCESS",

                    "severity":
                        "HIGH",

                    "description":
                        (
                            "Suspicious process detected: "
                            f"{name}"
                        ),

                    "process":
                        name,

                    "command":
                        command,
                }
            )


        if contains_suspicious_command(
            command
        ):

            alerts.append(
                {
                    "type":
                        "MALICIOUS_COMMAND",

                    "severity":
                        "CRITICAL",

                    "description":
                        (
                            "Suspicious command pattern detected"
                        ),

                    "process":
                        name,

                    "command":
                        command,
                }
            )

    return alerts
