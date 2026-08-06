"""
IOC Threat Hunter

Searches files and logs for
Indicators of Compromise.
"""

import re


class IOCHunter:
    """
    Searches data for IOCs.
    """


    def __init__(self, iocs):

        self.iocs = iocs



    def search(self, content):
        """
        Search content for known IOCs.
        """

        findings = []


        for ioc in self.iocs:

            if ioc in content:

                findings.append(
                    {
                        "indicator": ioc,
                        "found": True
                    }
                )


        return findings



    def extract_iocs(self, content):
        """
        Extract common IOC types.
        """

        results = {

            "ips": [],

            "domains": [],

            "hashes": []

        }


        results["ips"] = re.findall(
            r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
            content
        )


        results["domains"] = re.findall(
            r"\b[a-zA-Z0-9.-]+\.(?:com|net|org|io)\b",
            content
        )


        results["hashes"] = re.findall(
            r"\b[a-fA-F0-9]{64}\b",
            content
        )


        return results
