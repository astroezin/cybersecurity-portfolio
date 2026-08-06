"""
Threat Hunting Report Generator
"""

import json
from datetime import datetime
from pathlib import Path


class HuntReporter:
    """
    Creates JSON and Markdown reports.
    """


    def __init__(self, output_dir="reports"):

        self.output_dir = Path(output_dir)

        self.output_dir.mkdir(
            exist_ok=True
        )


    def generate_report(self, findings):

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )


        report = {

            "report_id":
                f"HUNT-{timestamp}",

            "generated":
                timestamp,

            "total_findings":
                len(findings),

            "findings":
                findings

        }


        json_file = (
            self.output_dir /
            f"hunt_report_{timestamp}.json"
        )


        md_file = (
            self.output_dir /
            f"hunt_report_{timestamp}.md"
        )


        with open(json_file, "w") as file:

            json.dump(
                report,
                file,
                indent=4
            )


        self.create_markdown(
            report,
            md_file
        )


        return {
            "json": json_file,
            "markdown": md_file
        }



    def create_markdown(
        self,
        report,
        filename
    ):

        content = []

        content.append(
            "# Threat Hunting Report\n"
        )


        content.append(
            f"## Report ID\n{report['report_id']}\n"
        )


        content.append(
            f"## Total Findings\n{report['total_findings']}\n"
        )


        content.append(
            "## Findings\n"
        )


        for index, finding in enumerate(
            report["findings"],
            start=1
        ):

            content.append(
                f"### Finding {index}\n"
            )

            content.append(
                "```json\n"
            )

            content.append(
                json.dumps(
                    finding,
                    indent=4
                )
            )

            content.append(
                "\n```\n"
            )


        with open(
            filename,
            "w"
        ) as file:

            file.write(
                "\n".join(content)
            )
