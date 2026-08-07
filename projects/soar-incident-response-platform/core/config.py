"""
Configuration settings for SOAR Incident Response Platform.
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


LOG_DIR = BASE_DIR / "logs"

REPORT_DIR = BASE_DIR / "reports"

CASE_DIR = BASE_DIR / "cases"

SAMPLE_DIR = BASE_DIR / "samples"


LOG_FILE = LOG_DIR / "soar.log"


REPORT_JSON = (
    REPORT_DIR /
    "incident_report.json"
)


REPORT_MARKDOWN = (
    REPORT_DIR /
    "incident_report.md"
)


CASE_DATABASE = (
    CASE_DIR /
    "cases.json"
)


def create_directories():
    """
    Create required application directories.
    """

    directories = [
        LOG_DIR,
        REPORT_DIR,
        CASE_DIR,
        SAMPLE_DIR,
    ]

    for directory in directories:

        directory.mkdir(
            parents=True,
            exist_ok=True
        )
