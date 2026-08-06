"""
Configuration module for Log Correlation Engine.
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    """
    Global application configuration.
    """

    TOOL_NAME = "Log Correlation Engine"

    SAMPLE_DIR = BASE_DIR / "samples"

    ALERT_DIR = BASE_DIR / "alerts"

    REPORT_DIR = BASE_DIR / "reports"

    LOG_TYPES = [
        "auth",
        "firewall",
        "application"
    ]


def ensure_directories():
    """
    Create required directories.
    """

    directories = [
        Config.ALERT_DIR,
        Config.REPORT_DIR
    ]

    for directory in directories:
        directory.mkdir(
            exist_ok=True
        )
