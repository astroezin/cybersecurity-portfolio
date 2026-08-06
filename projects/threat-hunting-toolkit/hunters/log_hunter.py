"""
Log Threat Hunter

Searches logs for suspicious
security activity.
"""


class LogHunter:
    """
    Performs log-based hunting.
    """


    def __init__(self):

        self.patterns = {

            "failed_login":
                "Failed password",

            "privilege_escalation":
                "sudo",

            "suspicious_download":
                "wget",

            "reverse_shell":
                "nc "

        }



    def hunt(self, logfile):
        """
        Search log file for patterns.
        """

        findings = []


        with open(
            logfile,
            "r"
        ) as file:


            for line_number, line in enumerate(
                file,
                start=1
            ):


                for name, pattern in self.patterns.items():


                    if pattern.lower() in line.lower():

                        findings.append(
                            {
                                "type": name,

                                "line":
                                    line_number,

                                "content":
                                    line.strip()
                            }
                        )


        return findings
