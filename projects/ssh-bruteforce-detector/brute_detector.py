#!/usr/bin/env python3

import argparse
import re
from collections import Counter

FAILED_REGEX = re.compile(
    r"Failed password for (?:invalid user )?(\S+) from (\S+)"
)

SUCCESS_REGEX = re.compile(
    r"Accepted password for (\S+) from (\S+)"
)


def analyze_log(filename):

    failed_ips = Counter()
    failed_users = Counter()
    successful = []

    with open(filename, "r") as log:

        for line in log:

            failed = FAILED_REGEX.search(line)

            if failed:
                username = failed.group(1)
                ip = failed.group(2)

                failed_ips[ip] += 1
                failed_users[username] += 1
                continue

            success = SUCCESS_REGEX.search(line)

            if success:
                successful.append(success.group(1))

    print("=" * 60)
    print("SSH Brute Force Detector")
    print("=" * 60)

    print("\nFailed Login Attempts by IP\n")

    for ip, count in failed_ips.items():
        print(f"{ip:<18} {count}")

    print("\nFailed Login Attempts by Username\n")

    for user, count in failed_users.items():
        print(f"{user:<18} {count}")

    print("\nSuccessful Logins\n")

    if successful:
        for user in successful:
            print(user)
    else:
        print("None")

    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)

    print(f"Total Failed Attempts : {sum(failed_ips.values())}")
    print(f"Unique IPs            : {len(failed_ips)}")
    print(f"Unique Users          : {len(failed_users)}")
    print(f"Successful Logins     : {len(successful)}")


def main():

    parser = argparse.ArgumentParser(
        description="SSH Brute Force Detector"
    )

    parser.add_argument(
        "logfile",
        help="Path to auth.log"
    )

    args = parser.parse_args()

    analyze_log(args.logfile)


if __name__ == "__main__":
    main()
