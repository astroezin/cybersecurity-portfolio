"""
Incident reporting module for SOAR Incident Response Platform.
"""

import json
from datetime import datetime

from core.config import (
    REPORT_JSON,
    REPORT_MARKDOWN,
)


def create_incident_report(
    incident,
):
    """
    Create incident report structure.

    Args:
        incident (dict): Incident details.

    Returns:
        dict: Formatted report.
    """

    return {

        "case_id":
            incident.get(
                "case_id",
                "UNKNOWN"
            ),

        "created":
            datetime.utcnow().isoformat(),

        "severity":
            incident.get(
                "severity",
                "UNKNOWN"
            ),

        "status":
            incident.get(
                "status",
                "UNKNOWN"
            ),

        "summary":
            incident.get(
                "summary",
                ""
            ),

        "detections":
            incident.get(
                "detections",
                []
            ),

        "actions":
            incident.get(
                "actions",
                []
            ),

        "mitre":
            incident.get(
                "mitre",
                []
            ),

        "risk":
            incident.get(
                "risk",
                {}
            ),

    }


def save_report(
    report
):
    """
    Save JSON and Markdown reports.

    Args:
        report (dict): Incident report.

    Returns:
        dict: Saved file paths.
    """

    with open(
        REPORT_JSON,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )


    markdown = generate_markdown(
        report
    )


    with open(
        REPORT_MARKDOWN,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            markdown
        )


    return {

        "json":
            REPORT_JSON,

        "markdown":
            REPORT_MARKDOWN,

    }


def generate_markdown(
    report
):
    """
    Generate Markdown incident report.

    Args:
        report (dict): Report data.

    Returns:
        str: Markdown content.
    """

    actions = "\n".join(
        [
            f"- {item}"
            for item in report.get(
                "actions",
                []
            )
        ]
    )


    mitre = "\n".join(
        [
            f"- {item}"
            for item in report.get(
                "mitre",
                []
            )
        ]
    )


    return f"""
# SOAR Incident Report

## Case ID

{report['case_id']}


## Severity

{report['severity']}


## Status

{report['status']}


## Summary

{report['summary']}


## Risk Assessment

Score: {report['risk'].get('score', 0)}

Level: {report['risk'].get('level', 'UNKNOWN')}


## Response Actions

{actions}


## MITRE ATT&CK Mapping

{mitre}

"""
