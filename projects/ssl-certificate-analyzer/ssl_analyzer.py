#!/usr/bin/env python3

import argparse
import socket
import ssl
from datetime import datetime


def get_certificate(hostname, port=443):
    context = ssl.create_default_context()

    with socket.create_connection((hostname, port), timeout=5) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()

            print("=" * 70)
            print(f"SSL Certificate Analysis: {hostname}")
            print("=" * 70)

            print(f"TLS Version : {ssock.version()}")
            print(f"Cipher Suite: {ssock.cipher()[0]}")

            print("\nIssuer")
            print("-" * 30)
            for item in cert.get("issuer", []):
                print(f"{item[0][0]} : {item[0][1]}")

            print("\nSubject")
            print("-" * 30)
            for item in cert.get("subject", []):
                print(f"{item[0][0]} : {item[0][1]}")

            print("\nValidity")
            print("-" * 30)

            not_before = cert["notBefore"]
            not_after = cert["notAfter"]

            print(f"Valid From : {not_before}")
            print(f"Valid Until: {not_after}")

            expiry = datetime.strptime(
                not_after,
                "%b %d %H:%M:%S %Y %Z"
            )

            days = (expiry - datetime.utcnow()).days

            print(f"Days Remaining: {days}")

            print("\nSubject Alternative Names")
            print("-" * 30)

            for san in cert.get("subjectAltName", []):
                print(san[1])


def main():
    parser = argparse.ArgumentParser(
        description="SSL Certificate Analyzer"
    )

    parser.add_argument(
        "host",
        help="Hostname"
    )

    args = parser.parse_args()

    try:
        get_certificate(args.host)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
