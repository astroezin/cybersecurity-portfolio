#!/usr/bin/env python3

import argparse
import socket
import ipaddress
import sys


def validate_ip(ip):
    """
    Validate IPv4 or IPv6 address.
    """
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def reverse_lookup(ip):
    """
    Perform reverse DNS lookup.
    """
    try:
        hostname, aliases, addresses = socket.gethostbyaddr(ip)

        print("=" * 60)
        print("Reverse DNS Lookup")
        print("=" * 60)

        print(f"IP Address : {ip}")
        print(f"Hostname   : {hostname}")

        if aliases:
            print(f"Aliases    : {', '.join(aliases)}")
        else:
            print("Aliases    : None")

        print(f"Addresses  : {', '.join(addresses)}")

    except socket.herror:
        print("No PTR record found for this IP address.")

    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Reverse DNS Lookup Tool"
    )

    parser.add_argument(
        "ip",
        help="IPv4 or IPv6 address"
    )

    args = parser.parse_args()

    if not validate_ip(args.ip):
        print("Invalid IP address.")
        sys.exit(1)

    reverse_lookup(args.ip)


if __name__ == "__main__":
    main()
