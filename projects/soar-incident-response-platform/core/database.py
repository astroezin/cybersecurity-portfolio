"""
Database handler for SOAR Incident Response Platform.
"""

import json

from pathlib import Path


def save_data(
    data,
    file_path: Path
):
    """
    Save data to JSON file.

    Args:
        data (dict/list): Data to save.
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


def load_data(
    file_path: Path
):
    """
    Load data from JSON file.

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


def append_data(
    item,
    file_path: Path
):
    """
    Append item to JSON list database.

    Args:
        item (dict): New record.
        file_path (Path): Database file.
    """

    records = load_data(
        file_path
    )


    if not isinstance(
        records,
        list
    ):

        records = []


    records.append(
        item
    )


    save_data(
        records,
        file_path
    )
