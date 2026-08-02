#!/usr/bin/env python3

import argparse
import json
import ipaddress
from pathlib import Path


def load_database():
    db = Path("iocs.json")

    with db.open("r") as file:
        return json.load(file)


def detect_type(value):

    try:
        ipaddress.ip_address(value)
        return "ips"
    except ValueError:
        pass

    if value.startswith("http://") or value.startswith("https://"):
        return "urls"

    if len(value) == 64:
        return "hashes"

    return "domains"


def check_ioc(value, database):

    category = detect_type(value)

    print("=" * 60)
    print("IOC Checker")
    print("=" * 60)

    print(f"\nIOC       : {value}")
    print(f"Category  : {category[:-1].upper()}")

    if value in database[category]:

        info = database[category][value]

        print("Status    : MALICIOUS")
        print(f"Threat    : {info['threat']}")
        print(f"Severity  : {info['severity']}")

    else:

        print("Status    : SAFE")
        print("Threat    : None Found")


def main():

    parser = argparse.ArgumentParser(
        description="Offline IOC Checker"
    )

    parser.add_argument(
        "ioc",
        help="IP, Domain, URL or SHA256 Hash"
    )

    args = parser.parse_args()

    database = load_database()

    check_ioc(args.ioc, database)


if __name__ == "__main__":
    main()
