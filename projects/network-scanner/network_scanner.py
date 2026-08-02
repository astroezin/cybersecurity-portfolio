#!/usr/bin/env python3

import argparse
import socket
from concurrent.futures import ThreadPoolExecutor

COMMON_SERVICES = {
    20: "FTP-DATA",
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP-ALT",
}


def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((host, port))
    sock.close()

    if result == 0:
        service = COMMON_SERVICES.get(port, "Unknown")
        print(f"[OPEN ] {port:<6} {service}")


def main():
    parser = argparse.ArgumentParser(
        description="Multi-threaded Network Scanner"
    )

    parser.add_argument(
        "host",
        help="Target IP or hostname"
    )

    parser.add_argument(
        "--start",
        type=int,
        default=1,
        help="Start port (default: 1)"
    )

    parser.add_argument(
        "--end",
        type=int,
        default=1024,
        help="End port (default: 1024)"
    )

    parser.add_argument(
        "--threads",
        type=int,
        default=100,
        help="Number of worker threads (default: 100)"
    )

    args = parser.parse_args()

    print("=" * 60)
    print(f"Scanning {args.host}")
    print("=" * 60)

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        for port in range(args.start, args.end + 1):
            executor.submit(scan_port, args.host, port)


if __name__ == "__main__":
    main()
