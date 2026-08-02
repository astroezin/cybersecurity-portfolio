#!/usr/bin/env python3

import argparse
import sys
import whois


def format_field(value):
    """
    Convert WHOIS values into readable text.
    """

    if value is None:
        return "Not Available"

    if isinstance(value, list):
        return ", ".join(str(v) for v in value)

    return str(value)


def lookup_domain(domain):
    """
    Retrieve WHOIS information for a domain.
    """

    try:
        info = whois.whois(domain)

        print("=" * 60)
        print(f"WHOIS INFORMATION : {domain}")
        print("=" * 60)

        print(f"Domain Name      : {format_field(info.domain_name)}")
        print(f"Registrar        : {format_field(info.registrar)}")
        print(f"Creation Date    : {format_field(info.creation_date)}")
        print(f"Expiration Date  : {format_field(info.expiration_date)}")
        print(f"Updated Date     : {format_field(info.updated_date)}")
        print(f"Name Servers     : {format_field(info.name_servers)}")
        print(f"Status           : {format_field(info.status)}")
        print(f"Emails           : {format_field(info.emails)}")
        print(f"DNSSEC           : {format_field(info.dnssec)}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():

    parser = argparse.ArgumentParser(
        description="Simple WHOIS Lookup Tool"
    )

    parser.add_argument(
        "domain",
        help="Target domain"
    )

    args = parser.parse_args()

    lookup_domain(args.domain)


if __name__ == "__main__":
    main()
