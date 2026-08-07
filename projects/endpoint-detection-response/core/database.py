"""
Local storage handler for Endpoint Detection & Response Simulator.
"""

import json

from pathlib import Path


def save_json(
    data,
    file_path: Path
):
    """
    Save data as JSON.

    Args:
        data (dict/list): Data to store.
        file_path (Path): Destination file.
    """

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def load_json(
    file_path: Path
):
    """
    Load JSON data.

    Args:
        file_path (Path): JSON file.

    Returns:
        dict/list
    """

    if not file_path.exists():

        return []

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(
            file
        )
