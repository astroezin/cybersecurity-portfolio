#!/usr/bin/env python3

import socket
import sys


def scan_port(host, port):
    """Scan a single TCP port."""

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)

            result = s.connect_ex((host, port))

            if result == 0:
                print(f"[+] Port {port} is OPEN")
            else:
                print(f"[-] Port {port} is CLOSED")

    except KeyboardInterrupt:
        print("\nScan cancelled.")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("python3 scanner.py <host> <port1> [port2 port3 ...]")
        sys.exit()

    host = sys.argv[1]

    print("=" * 40)
    print(f"Scanning {host}")
    print("=" * 40)

    for port in sys.argv[2:]:
        scan_port(host, int(port))


if __name__ == "__main__":
    main()
