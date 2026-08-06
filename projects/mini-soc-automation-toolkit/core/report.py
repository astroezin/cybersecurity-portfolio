"""
Report generation module.

Creates JSON and Markdown security reports.
"""

import json
from datetime import datetime

from core.config import Config


def generate_filename(extension):
    """
    Create timestamp based filename.
    """

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    return (
        Config.REPORT_DIRECTORY
        /
        f"soc_report_{timestamp}.{extension}"
    )


def save_json_report(data):
    """
    Save investigation results as JSON.
    """

    filepath = generate_filename(
        "json"
    )

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    return filepath



def save_markdown_report(data):
    """
    Save investigation results as Markdown.
    """

    filepath = generate_filename(
        "md"
    )

    risk = data.get(
        "risk",
        {}
    )

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "# SOC Analysis Report\n\n"
        )

        file.write(
            f"## IOC\n\n"
            f"{data.get('ioc')}\n\n"
        )

        file.write(
            f"## Type\n\n"
            f"{data.get('type')}\n\n"
        )

        file.write(
            "## Risk Assessment\n\n"
        )

        file.write(
            f"Risk Level: "
            f"**{risk.get('risk')}**\n\n"
        )

        file.write(
            f"Risk Score: "
            f"{risk.get('score')}\n\n"
        )

        file.write(
            "## Risk Factors\n\n"
        )

        for reason in risk.get(
            "reasons",
            []
        ):

            file.write(
                f"- {reason}\n"
            )

        file.write(
            "\n## Generated\n\n"
        )

        file.write(
            datetime.now().isoformat()
        )

    return filepath
