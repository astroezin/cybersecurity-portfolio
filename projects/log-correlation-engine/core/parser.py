"""
Log parsing engine.

Converts raw security logs into structured events.
"""

import re


class LogParser:
    """
    Parses different security log formats.
    """


    def parse_auth_log(self, line):
        """
        Parse Linux authentication logs.
        """

        event = {
            "raw": line,
            "event_type": "unknown",
            "username": None,
            "source_ip": None,
            "severity": "low"
        }


        failed_login = re.search(
            r"Failed password for (\w+) from ([\d.]+)",
            line
        )


        if failed_login:

            event["event_type"] = "failed_login"

            event["username"] = (
                failed_login.group(1)
            )

            event["source_ip"] = (
                failed_login.group(2)
            )

            event["severity"] = "medium"

            return event



        successful_login = re.search(
            r"Accepted password for (\w+) from ([\d.]+)",
            line
        )


        if successful_login:

            event["event_type"] = "successful_login"

            event["username"] = (
                successful_login.group(1)
            )

            event["source_ip"] = (
                successful_login.group(2)
            )

            event["severity"] = "low"

            return event



        sudo_event = re.search(
            r"sudo: (\w+) .* COMMAND=(.*)",
            line
        )


        if sudo_event:

            event["event_type"] = "sudo_command"

            event["username"] = (
                sudo_event.group(1)
            )

            event["command"] = (
                sudo_event.group(2)
            )

            event["severity"] = "high"

            return event


        return event
