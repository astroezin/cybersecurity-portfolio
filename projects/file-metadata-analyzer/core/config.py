"""
Configuration settings
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


REPORT_DIR = BASE_DIR / "reports"

LOG_DIR = BASE_DIR / "logs"


LOG_FILE = LOG_DIR / "metadata_analyzer.log"


TOOL_NAME = "File Metadata Analyzer"



def ensure_directories():

    REPORT_DIR.mkdir(
        exist_ok=True
    )


    LOG_DIR.mkdir(
        exist_ok=True
    )
