#!/usr/bin/env python3

import argparse
import json
import socket
import ssl
from datetime import datetime, UTC
from pathlib import Path


def get_certificate(hostname, port):
    """
    Retrieve SSL/TLS certificate from a remote server.
    """

    context = ssl.create_default_context()

    with socket.create_connection(
        (hostname, port),
        timeout=5
    ) as sock:

        with context.wrap_socket(
            sock,
            server_hostname=hostname
        ) as secure_sock:

            return secure_sock.getpeercert()


def parse_name(name):
    """
    Convert certificate tuples into a readable string.
    """

    values = []

    for item in name:
        for key, value in item:
            values.append(f"{key}={value}")

    return ", ".join(values)


def parse_san(certificate):
    """
    Extract Subject Alternative Names.
    """

    san = certificate.get(
        "subjectAltName",
        []
    )

    return [entry[1] for entry in san]


def calculate_days_remaining(expiry):
    """
    Calculate certificate expiration.
    """

    expires = datetime.strptime(
        expiry,
        "%b %d %H:%M:%S %Y %Z"
    )

    expires = expires.replace(tzinfo=UTC)

    remaining = expires - datetime.now(UTC)

    return remaining.days

def generate_report(data, output_file):
    """
    Save JSON report.
    """

    path = Path(output_file)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with path.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def display_results(report):

    print("=" * 60)
    print("SSL/TLS Certificate Analyzer")
    print("=" * 60)

    print(f"Host               : {report['host']}")
    print(f"Port               : {report['port']}")
    print()

    print(f"Subject            : {report['subject']}")
    print(f"Issuer             : {report['issuer']}")
    print(f"Serial Number      : {report['serial_number']}")
    print(f"Version            : {report['version']}")
    print()

    print(f"Valid From         : {report['valid_from']}")
    print(f"Valid Until        : {report['valid_until']}")
    print(f"Days Remaining     : {report['days_remaining']}")
    print()

    print("Subject Alternative Names")
    print("-" * 60)

    for name in report["subject_alt_names"]:
        print(name)

    print()
    print(f"JSON Report Saved  : {report['report_file']}")


def main():

    parser = argparse.ArgumentParser(
        description=(
            "SSL/TLS Certificate Analyzer"
        )
    )

    parser.add_argument(
        "-H",
        "--host",
        required=True,
        help="Target hostname"
    )

    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=443,
        help="Target port"
    )

    parser.add_argument(
        "-o",
        "--output",
        default="reports/certificate_report.json",
        help="Output JSON report"
    )

    args = parser.parse_args()

    try:

        certificate = get_certificate(
            args.host,
            args.port
        )

        report = {
            "host": args.host,
            "port": args.port,
            "subject": parse_name(
                certificate["subject"]
            ),
            "issuer": parse_name(
                certificate["issuer"]
            ),
            "serial_number": certificate.get(
                "serialNumber",
                "Unknown"
            ),
            "version": certificate.get(
                "version",
                "Unknown"
            ),
            "valid_from": certificate.get(
                "notBefore"
            ),
            "valid_until": certificate.get(
                "notAfter"
            ),
            "days_remaining": calculate_days_remaining(
                certificate["notAfter"]
            ),
            "subject_alt_names": parse_san(
                certificate
            ),
            "scan_time": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "report_file": args.output
        }

        generate_report(
            report,
            args.output
        )

        display_results(
            report
        )

    except ssl.SSLError as error:
        print(f"[SSL ERROR] {error}")

    except socket.gaierror:
        print("[ERROR] Unable to resolve hostname.")

    except TimeoutError:
        print("[ERROR] Connection timed out.")

    except ConnectionRefusedError:
        print("[ERROR] Connection refused.")

    except Exception as error:
        print(f"[ERROR] {error}")


if __name__ == "__main__":
    main()
