"""
Incident report generator.

Creates JSON and Markdown reports.
"""

import json
from datetime import datetime
from pathlib import Path

from core.config import Config


class ReportGenerator:
    """
    Generates SOC investigation reports.
    """


    def save_json(self, data):
        """
        Save JSON incident report.
        """

        filename = (
            Config.REPORT_DIR /
            f"incident_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )


        with open(
            filename,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )


        return filename



    def save_markdown(self, data):
        """
        Save Markdown incident report.
        """

        filename = (
            Config.REPORT_DIR /
            f"incident_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        )


        incident = data["incident"]
        alert = data["alert"]
        timeline = data["timeline"]


        content = f"""
# Security Incident Report


## Incident

{incident.get("incident")}


## Severity

{incident.get("severity")}


## Risk Score

{alert.get("risk_score")}/100


## Risk Level

{alert.get("risk_level")}


## MITRE ATT&CK

"""


        for technique in incident.get("mitre", []):

            content += f"- {technique}\n"


        content += """

## Timeline

"""


        for event in timeline:

            content += (
                f"{event['step']}. "
                f"{event['event']} "
                f"({event.get('user')})\n"
            )


        with open(
            filename,
            "w"
        ) as file:

            file.write(content)


        return filename
