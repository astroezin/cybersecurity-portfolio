"""
Detection rules engine.

Analyzes normalized events
and generates security alerts.
"""

from collections import defaultdict


class DetectionRules:
    """
    Contains SOC detection logic.
    """


    def __init__(self):

        self.failed_login_tracker = defaultdict(int)


    def check_failed_logins(self, event):
        """
        Detect brute force attempts.
        """

        alerts = []


        if event["event_type"] == "failed_login":

            ip = event["source_ip"]

            self.failed_login_tracker[ip] += 1


            if self.failed_login_tracker[ip] >= 5:

                alerts.append(
                    {
                        "alert":
                            "SSH Brute Force Detected",

                        "severity":
                            "HIGH",

                        "source_ip":
                            ip,

                        "mitre":
                            "T1110",

                        "description":
                            "Multiple failed SSH login attempts detected"
                    }
                )


        return alerts



    def check_privilege_escalation(self, event):
        """
        Detect suspicious sudo activity.
        """

        alerts = []


        if event["event_type"] == "sudo_command":

            alerts.append(
                {
                    "alert":
                        "Privilege Escalation Activity",

                    "severity":
                        "HIGH",

                    "user":
                        event.get("username"),

                    "command":
                        event.get("command"),

                    "mitre":
                        "T1548",

                    "description":
                        "User executed privileged command"
                }
            )


        return alerts



    def analyze_event(self, event):
        """
        Run all detection rules.
        """

        alerts = []

        alerts.extend(
            self.check_failed_logins(event)
        )

        alerts.extend(
            self.check_privilege_escalation(event)
        )


        return alerts
