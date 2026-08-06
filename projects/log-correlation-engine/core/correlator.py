"""
Event correlation engine.

Combines multiple alerts/events
to identify security incidents.
"""


class CorrelationEngine:
    """
    Correlates security events.
    """


    def __init__(self):

        self.events = []


    def add_event(self, event):
        """
        Store event for correlation.
        """

        self.events.append(event)



    def detect_account_compromise(self):
        """
        Detect possible account takeover.

        Pattern:

        Failed login attempts
        +
        Successful login
        +
        Privileged command
        """

        failed_login = False
        successful_login = False
        sudo_activity = False


        for event in self.events:

            if event.get("event_type") == "failed_login":
                failed_login = True


            if event.get("event_type") == "successful_login":
                successful_login = True


            if event.get("event_type") == "sudo_command":
                sudo_activity = True



        if (
            failed_login
            and successful_login
            and sudo_activity
        ):

            return {

                "incident":
                    "Possible Account Compromise",

                "severity":
                    "CRITICAL",

                "description":
                    "Multiple failed logins followed by successful login and privileged activity",

                "mitre":
                    [
                        "T1110",
                        "T1078",
                        "T1548"
                    ]
            }


        return None



    def analyze(self):
        """
        Run correlation checks.
        """

        incidents = []

        compromise = (
            self.detect_account_compromise()
        )


        if compromise:

            incidents.append(
                compromise
            )


        return incidents
