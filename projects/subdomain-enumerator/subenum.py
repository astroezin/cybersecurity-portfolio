#!/usr/bin/env python3

import argparse
import socket
import time


def resolve_subdomain(subdomain, domain, timeout=2):
    """
    Resolve a subdomain to its IPv4 address.
    Returns the IP address if successful, otherwise None.
    """
    hostname = f"{subdomain}.{domain}"

    try:
        socket.setdefaulttimeout(timeout)
        ip = socket.gethostbyname(hostname)
        return hostname, ip
    except socket.gaierror:
        return None
    except Exception:
        return None


def load_wordlist(filename):
    """
    Load subdomains from a wordlist.
    """
    with open(filename, "r") as file:
        return [
            line.strip()
            for line in file
            if line.strip() and not line.startswith("#")
        ]


def main():
    parser = argparse.ArgumentParser(
        description="Simple Subdomain Enumerator"
    )

    parser.add_argument(
        "domain",
        help="Target domain (example.com)"
    )

    parser.add_argument(
        "--wordlist",
        default="wordlist.txt",
        help="Path to wordlist"
    )

    args = parser.parse_args()

    print("=" * 55)
    print("Simple Subdomain Enumerator")
    print("=" * 55)
    print(f"Target : {args.domain}")

    try:
        subdomains = load_wordlist(args.wordlist)
    except FileNotFoundError:
        print(f"[-] Wordlist not found: {args.wordlist}")
        return

    found = []

    start = time.time()

    for sub in subdomains:
        result = resolve_subdomain(sub, args.domain)

        if result:
            hostname, ip = result
            print(f"[FOUND] {hostname:<35} {ip}")
            found.append(result)

    end = time.time()

    print("\n" + "=" * 55)
    print("Scan Summary")
    print("=" * 55)
    print(f"Subdomains Tested : {len(subdomains)}")
    print(f"Found             : {len(found)}")
    print(f"Time              : {end - start:.2f} seconds")


if __name__ == "__main__":
    main()
