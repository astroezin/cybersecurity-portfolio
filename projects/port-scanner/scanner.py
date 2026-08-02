#!/usr/bin/env python3

import argparse
import socket
import sys


def get_service_name(port):
    """
    Return the common service name for a port.
    """
    try:
        return socket.getservbyport(port)
    except OSError:
        return "Unknown"


def scan_port(host, port, timeout=1):
    """
    Scan a single TCP port.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)

            result = sock.connect_ex((host, port))

            service = get_service_name(port)

            if result == 0:
                print(f"[OPEN ] {port:<5} {service}")
            else:
                print(f"[CLOSED] {port:<5} {service}")

    except KeyboardInterrupt:
        print("\nScan interrupted.")
        sys.exit(1)

    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit(1)

    except Exception as e:
        print(f"Error scanning port {port}: {e}")


def parse_ports(port_argument):
    """
    Convert user input into a list of ports.

    Supported:
        80
        22,80,443
        20-25
    """

    ports = []

    if "-" in port_argument:
        start, end = port_argument.split("-")

        ports.extend(range(int(start), int(end) + 1))

    elif "," in port_argument:
        ports.extend(int(p.strip()) for p in port_argument.split(","))

    else:
        ports.append(int(port_argument))

    return ports


def scan_host(host, ports):
    """
    Scan all requested ports.
    """
    print("=" * 45)
    print(f"Scanning Host : {host}")
    print("=" * 45)

    for port in ports:
        scan_port(host, port)


def main():
    parser = argparse.ArgumentParser(
        description="Simple Python TCP Port Scanner"
    )

    parser.add_argument(
        "host",
        help="Target hostname or IP address"
    )

    parser.add_argument(
        "ports",
        help="Port(s): 80 | 22,80,443 | 20-100"
    )

    args = parser.parse_args()

    ports = parse_ports(args.ports)

    scan_host(args.host, ports)


if __name__ == "__main__":
    main()
