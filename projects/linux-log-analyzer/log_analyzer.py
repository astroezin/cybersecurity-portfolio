#!/usr/bin/env python3

import argparse
import re
from collections import Counter


FAILED_PATTERN = re.compile(
    r"Failed password for (?:invalid user )?(\S+) from (\S+)"
)

SUCCESS_PATTERN = re.compile(
    r"Accepted (?:password|publickey) for (\S+) from (\S+)"
)


def analyze_log(logfile):
    failed = Counter()
    successful = Counter()

    with open(logfile, "r", encoding="utf-8") as file:
        for line in file:
            fail_match = FAILED_PATTERN.search(line)
            if fail_match:
                user, ip = fail_match.groups()
                failed[(user, ip)] += 1
                continue

            success_match = SUCCESS_PATTERN.search(line)
            if success_match:
                user, ip = success_match.groups()
                successful[(user, ip)] += 1

    print("=" * 60)
    print("Linux Authentication Log Analysis")
    print("=" * 60)

    print("\nFailed Logins")
    if failed:
        for (user, ip), count in failed.items():
            print(f"{user:15} {ip:15} Attempts: {count}")
    else:
        print("None")

    print("\nSuccessful Logins")
    if successful:
        for (user, ip), count in successful.items():
            print(f"{user:15} {ip:15} Logins: {count}")
    else:
        print("None")


def main():
    parser = argparse.ArgumentParser(
        description="Linux Authentication Log Analyzer"
    )

    parser.add_argument(
        "logfile",
        help="Path to auth.log file"
    )

    args = parser.parse_args()

    analyze_log(args.logfile)


if __name__ == "__main__":
    main()
