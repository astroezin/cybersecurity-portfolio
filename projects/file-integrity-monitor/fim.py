#!/usr/bin/env python3

import argparse
import hashlib
import json
import os
import sys

BASELINE_FILE = "baseline.json"


def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


def scan_directory(directory):
    hashes = {}

    for root, _, files in os.walk(directory):
        for filename in files:
            path = os.path.join(root, filename)

            try:
                hashes[path] = calculate_hash(path)
            except Exception:
                pass

    return hashes


def create_baseline(directory):
    hashes = scan_directory(directory)

    with open(BASELINE_FILE, "w") as file:
        json.dump(hashes, file, indent=4)

    print(f"\nBaseline saved to {BASELINE_FILE}")


def compare(directory):
    if not os.path.exists(BASELINE_FILE):
        print("Baseline not found.")
        sys.exit(1)

    with open(BASELINE_FILE) as file:
        baseline = json.load(file)

    current = scan_directory(directory)

    print("\nChecking integrity...\n")

    for path, current_hash in current.items():

        if path not in baseline:
            print(f"[NEW] {path}")

        elif baseline[path] != current_hash:
            print(f"[MODIFIED] {path}")

    for path in baseline:

        if path not in current:
            print(f"[DELETED] {path}")

    print("\nDone.")


def main():

    parser = argparse.ArgumentParser(
        description="File Integrity Monitor"
    )

    parser.add_argument(
        "mode",
        choices=["baseline", "check"]
    )

    parser.add_argument(
        "directory"
    )

    args = parser.parse_args()

    if args.mode == "baseline":
        create_baseline(args.directory)

    else:
        compare(args.directory)


if __name__ == "__main__":
    main()
