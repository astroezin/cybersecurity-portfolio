#!/usr/bin/env python3
"""
Threat Intelligence Lookup

Look up IP reputation using VirusTotal and AbuseIPDB.
"""

import argparse
import sys

from api.abuseipdb import (
    lookup_ip as abuse_lookup_ip,
    AbuseIPDBError,
)
from api.virustotal import (
    lookup_ip as vt_lookup_ip,
    VirusTotalError,
)
from utils.config import validate_api_keys
from utils.formatter import (
    format_abuseipdb_ip,
    format_virustotal_ip,
)
from utils.validators import detect_ioc_type


def main():
    parser = argparse.ArgumentParser(
        description="Threat Intelligence Lookup Tool"
    )

    parser.add_argument(
        "target",
        help="IP address, domain, URL, or hash"
    )

    args = parser.parse_args()

    try:
        validate_api_keys()

        ioc_type = detect_ioc_type(args.target)

        if ioc_type != "ip":
            print(
                f"[!] IOC type '{ioc_type}' "
                "is not supported in Version 1."
            )
            print(
                "Version 1 supports IPv4 lookups only."
            )
            sys.exit(1)

        print("=" * 50)
        print("Threat Intelligence Lookup")
        print("=" * 50)
        print(f"Target : {args.target}")
        print()

        vt_data = vt_lookup_ip(args.target)
        print(format_virustotal_ip(vt_data))
        print()

        abuse_data = abuse_lookup_ip(args.target)
        print(format_abuseipdb_ip(abuse_data))

    except (VirusTotalError, AbuseIPDBError) as exc:
        print(f"[ERROR] {exc}")
        sys.exit(1)

    except Exception as exc:
        print(f"[ERROR] {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
