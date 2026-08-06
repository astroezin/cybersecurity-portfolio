#!/usr/bin/env python3
"""
Security Report Generator

Generate professional Markdown security reports from JSON findings.
"""

import argparse
import json
import sys
from pathlib import Path

from report_builder import generate_markdown


def load_json(filepath):
    """
    Load a JSON file.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
        sys.exit(1)
    except json.JSONDecodeError as exc:
        print(f"[ERROR] Invalid JSON: {exc}")
        sys.exit(1)


def save_report(content, output_file):
    """
    Save the generated report.
    """
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)


def main():
    parser = argparse.ArgumentParser(
        description="Generate professional Markdown security reports."
    )

    parser.add_argument(
        "input",
        help="Input JSON file containing security findings."
    )

    parser.add_argument(
        "-o",
        "--output",
        default="reports/security_report.md",
        help="Output Markdown report."
    )

    args = parser.parse_args()

    data = load_json(args.input)

    report = generate_markdown(data)

    save_report(report, args.output)

    print("=" * 50)
    print("Security Report Generator")
    print("=" * 50)
    print(f"Input File : {args.input}")
    print(f"Output File: {args.output}")
    print()
    print("[+] Report generated successfully.")


if __name__ == "__main__":
    main()
