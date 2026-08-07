"""
Incident report generator for Endpoint Detection & Response Simulator.
"""

import json
from datetime import datetime
from uuid import uuid4

from core.config import (
    REPORT_JSON,
    REPORT_MARKDOWN,
)


def generate_incident_id():
    """
    Generate unique incident identifier.

    Returns:
        str
    """

    timestamp = datetime.now().strftime(
        "%Y%m%d"
    )

    return (
        f"EDR-{timestamp}-"
        f"{uuid4().hex[:6]}"
    )


def save_json_report(
    report
):
    """
    Save JSON incident report.

    Args:
        report (dict)
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


def save_markdown_report(
    report
):
    """
    Save Markdown incident report.

    Args:
        report (dict)
    """

    with open(
        REPORT_MARKDOWN,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "# EDR Incident Report\n\n"
        )

        file.write(
            f"## Incident ID\n"
            f"{report['incident_id']}\n\n"
        )

        file.write(
            f"## Severity\n"
            f"{report['risk']['level']}\n\n"
        )

        file.write(
            "## Detection Summary\n\n"
        )

        for alert in report["detections"]:

            file.write(
                f"- {alert['description']}\n"
            )

        file.write(
            "\n## MITRE ATT&CK Mapping\n\n"
        )

        for technique in report["mitre"]:

            file.write(
                f"- {technique}\n"
            )


def create_report(
    detections,
    risk,
    mitre
):
    """
    Create complete incident report.

    Args:
        detections (list)
        risk (dict)
        mitre (list)

    Returns:
        dict
    """

    return {
        "incident_id":
            generate_incident_id(),

        "timestamp":
            datetime.now().isoformat(),

        "risk":
            risk,

        "detections":
            detections,

        "mitre":
            mitre,
    }


def save_report(
    report
):
    """
    Save all report formats.

    Args:
        report (dict)
    """

    save_json_report(
        report
    )

    save_markdown_report(
        report
    )

    return {
        "json":
            REPORT_JSON,

        "markdown":
            REPORT_MARKDOWN,
    }
