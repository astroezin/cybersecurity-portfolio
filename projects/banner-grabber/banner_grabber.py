#!/usr/bin/env python3

import argparse
import socket
import sys


def grab_banner(host, port, timeout=3):
    """
    Connect to a TCP service and display its banner.
    """

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            sock.connect((host, port))

            # Send a HEAD request for common HTTP ports.
            if port in (80, 8080):
                request = f"HEAD / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
                sock.sendall(request.encode())

            try:
                data = sock.recv(4096)
            except socket.timeout:
                print("No banner received before timeout.")
                return

            if data:
                print("=" * 60)
                print(f"Banner from {host}:{port}")
                print("=" * 60)
                print(data.decode(errors="replace"))
            else:
                print("Connected, but no banner was returned.")

    except socket.timeout:
        print("Connection timed out.")

    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit(1)

    except ConnectionRefusedError:
        print("Connection refused.")

    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Simple TCP Banner Grabber"
    )

    parser.add_argument(
        "host",
        help="Target hostname or IP address"
    )

    parser.add_argument(
        "port",
        type=int,
        help="Target TCP port"
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=3,
        help="Connection timeout in seconds (default: 3)"
    )

    args = parser.parse_args()

    grab_banner(args.host, args.port, args.timeout)


if __name__ == "__main__":
    main()
