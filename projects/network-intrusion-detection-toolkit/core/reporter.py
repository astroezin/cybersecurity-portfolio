"""
Report generation module for the Network Intrusion Detection Toolkit.
"""

import json
from datetime import datetime
from pathlib import Path
from uuid import uuid4

from core.config import REPORT_DIR


def generate_case_id():
    """
    Generate unique investigation case ID.

    Returns:
        str
    """

    timestamp = datetime.now().strftime(
        "%Y%m%d"
    )

    return (
        f"CASE-{timestamp}-"
        f"{uuid4().hex[:8]}"
    )


def generate_report(
    data
):
    """
    Generate JSON report.

    Args:
        data (dict): Report data.

    Returns:
        Path
    """

    REPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    filename = (
        "nids_report_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        ".json"
    )

    report_path = REPORT_DIR / filename

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            default=str
        )

    return report_path


def create_report(
    packets,
    alerts,
    statistics,
    iocs,
    timeline
):
    """
    Create complete investigation report.

    Args:
        packets (list)
        alerts (list)
        statistics (dict)
        iocs (dict)
        timeline (list)

    Returns:
        dict
    """

    return {
        "case_information": {
            "case_id":
                generate_case_id(),

            "created":
                datetime.now().isoformat(),
        },

        "network_summary": {
            "total_packets":
                len(packets),

            "statistics":
                statistics,
        },

        "security_alerts":
            alerts,

        "indicators_of_compromise":
            iocs,

        "timeline":
            timeline,
    }


def save_report(
    report_data
):
    """
    Save report and return location.

    Args:
        report_data (dict)

    Returns:
        Path
    """

    return generate_report(
        report_data
    )
