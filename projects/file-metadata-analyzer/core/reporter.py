"""
Professional forensic report generator
"""

import json
from datetime import datetime

from core.config import REPORT_DIR



def generate_report(data):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


    json_file = REPORT_DIR / (
        f"metadata_report_{timestamp}.json"
    )


    markdown_file = REPORT_DIR / (
        f"metadata_report_{timestamp}.md"
    )


    with open(
        json_file,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


    create_markdown(
        data,
        markdown_file
    )


    return {

        "json": json_file,

        "markdown": markdown_file

    }



def create_markdown(data, file_path):

    lines = []


    lines.append(
        "# File Metadata Analyzer Report\n"
    )


    lines.append(
        "## Case Information\n"
    )


    lines.append(
        f"- **Case ID:** {data['case']['case_id']}"
    )


    lines.append(
        f"- **Created:** {data['case']['created']}"
    )


    lines.append(
        "\n## Evidence\n"
    )


    lines.append(
        f"- **Evidence ID:** {data['evidence']['evidence_id']}"
    )


    lines.append(
        f"- **File:** {data['evidence']['file']}"
    )


    lines.append(
        "\n## File Metadata\n"
    )


    for key, value in data["metadata"].items():

        lines.append(
            f"- **{key}:** {value}"
        )



    lines.append(
        "\n## File Hashes\n"
    )


    for key, value in data["hashes"].items():

        lines.append(
            f"- **{key.upper()}:** {value}"
        )



    lines.append(
        "\n## Security Analysis\n"
    )


    lines.append(
        f"- **Entropy:** {data['analysis']['entropy']}"
    )


    lines.append(
        "\n### Suspicious Findings\n"
    )


    findings = data["analysis"]["suspicious_metadata"]


    if findings:

        for item in findings:

            lines.append(
                f"- {item}"
            )

    else:

        lines.append(
            "- None"
        )



    lines.append(
        "\n## Timeline\n"
    )


    for event in data["timeline"]:

        lines.append(
            f"- {event['event']} : {event['timestamp']}"
        )



    lines.append(
        "\n## Chain of Custody\n"
    )


    for item in data["evidence"]["chain_of_custody"]:

        lines.append(
            f"- {item['action']} : {item['time']}"
        )


    with open(
        file_path,
        "w"
    ) as file:

        file.write(
            "\n".join(lines)
        )
