"""
Configuration settings for Endpoint Detection & Response Simulator.
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


LOG_DIR = BASE_DIR / "logs"

REPORT_DIR = BASE_DIR / "reports"

SAMPLE_DIR = BASE_DIR / "samples"


LOG_FILE = LOG_DIR / "edr.log"


REPORT_JSON = (
    REPORT_DIR /
    "edr_incident_report.json"
)


REPORT_MARKDOWN = (
    REPORT_DIR /
    "edr_incident_report.md"
)


def create_directories():
    """
    Create required project directories.
    """

    directories = [
        LOG_DIR,
        REPORT_DIR,
        SAMPLE_DIR,
    ]

    for directory in directories:

        directory.mkdir(
            parents=True,
            exist_ok=True
        )
