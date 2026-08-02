#!/usr/bin/env python3

import argparse
import requests

SECURITY_HEADERS = {
    "Strict-Transport-Security": "HTTPS enforcement",
    "Content-Security-Policy": "XSS protection",
    "X-Frame-Options": "Clickjacking protection",
    "X-Content-Type-Options": "MIME sniffing protection",
    "Referrer-Policy": "Referrer privacy",
    "Permissions-Policy": "Browser feature control",
}


def analyze_headers(url):
    try:
        response = requests.get(url, timeout=10)

        print("=" * 70)
        print(f"HTTP Header Analysis: {url}")
        print("=" * 70)

        print(f"Status Code : {response.status_code}")
        print(f"Server      : {response.headers.get('Server', 'Unknown')}")
        print()

        print("Security Headers")
        print("-" * 70)

        for header, description in SECURITY_HEADERS.items():
            value = response.headers.get(header)

            if value:
                print(f"[FOUND ] {header}")
                print(f"         {value}")
            else:
                print(f"[MISSING] {header}")

            print(f"         Purpose: {description}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="HTTP Security Header Analyzer"
    )

    parser.add_argument(
        "url",
        help="Target URL (include http:// or https://)"
    )

    args = parser.parse_args()

    analyze_headers(args.url)


if __name__ == "__main__":
    main()
