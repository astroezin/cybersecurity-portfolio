#!/usr/bin/env python3

import argparse
import socket
import sys


def resolve_hostname(hostname):
    """
    Resolve IPv4 and IPv6 addresses for a hostname.
    """

    try:
        results = socket.getaddrinfo(hostname, None)

        ipv4 = set()
        ipv6 = set()

        for result in results:
            family = result[0]
            address = result[4][0]

            if family == socket.AF_INET:
                ipv4.add(address)

            elif family == socket.AF_INET6:
                ipv6.add(address)

        print("=" * 50)
        print(f"Hostname : {hostname}")
        print("=" * 50)

        canonical = socket.getfqdn(hostname)
        print(f"Canonical Name : {canonical}")

        print("\nIPv4 Addresses")
        print("----------------")

        if ipv4:
            for ip in sorted(ipv4):
                print(ip)
        else:
            print("None")

        print("\nIPv6 Addresses")
        print("----------------")

        if ipv6:
            for ip in sorted(ipv6):
                print(ip)
        else:
            print("None")

    except socket.gaierror:
        print("Unable to resolve hostname.")
        sys.exit(1)

    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="DNS Lookup Tool"
    )

    parser.add_argument(
        "hostname",
        help="Target hostname"
    )

    args = parser.parse_args()

    resolve_hostname(args.hostname)


if __name__ == "__main__":
    main()
