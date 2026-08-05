"""
reporter.py

Displays analysis results.
"""

from modules.utils import get_service_name

SEPARATOR = "=" * 60


def print_banner(file_path, packet_count):
    print(SEPARATOR)
    print("PCAP Analyzer")
    print(SEPARATOR)
    print(f"Capture File : {file_path}")
    print(f"Total Packets: {packet_count}")


def print_protocols(protocols):
    print()
    print(SEPARATOR)
    print("Protocol Distribution")
    print(SEPARATOR)

    for protocol, count in sorted(
        protocols.items(),
        key=lambda item: item[1],
        reverse=True,
    ):
        print(f"{protocol:<12} {count}")


def print_ip_statistics(title, ip_counter):
    print()
    print(SEPARATOR)
    print(title)
    print(SEPARATOR)

    if not ip_counter:
        print("No IP packets found.")
        return

    for ip, count in ip_counter.most_common(10):
        print(f"{ip:<20} {count}")


def print_conversations(conversations):
    print()
    print(SEPARATOR)
    print("Top Conversations")
    print(SEPARATOR)

    if not conversations:
        print("No conversations found.")
        return

    for (src, dst), count in conversations.most_common(10):
        print(f"{src:<15} -> {dst:<15} {count}")


def print_ports(title, ports):
    print()
    print(SEPARATOR)
    print(title)
    print(SEPARATOR)

    if not ports:
        print("No ports found.")
        return

    print(f"{'Port':<8}{'Service':<20}{'Count'}")
    print("-" * 40)

    for port, count in ports.most_common(10):
        service = get_service_name(port)
        print(f"{port:<8}{service:<20}{count}")


def print_packet_sizes(stats):
    print()
    print(SEPARATOR)
    print("Packet Size Statistics")
    print(SEPARATOR)

    print(f"Total Bytes         : {stats['total_bytes']}")
    print(f"Smallest Packet     : {stats['smallest']} bytes")
    print(f"Largest Packet      : {stats['largest']} bytes")
    print(f"Average Packet Size : {stats['average']:.2f} bytes")
    
def print_capture_statistics(stats):
    """
    Display capture timing statistics.
    """
    print()
    print(SEPARATOR)
    print("Capture Statistics")
    print(SEPARATOR)

    print(
        f"Start Time       : "
        f"{stats['start'].strftime('%Y-%m-%d %H:%M:%S')}"
    )

    print(
        f"End Time         : "
        f"{stats['end'].strftime('%Y-%m-%d %H:%M:%S')}"
    )

    print(
        f"Duration         : "
        f"{stats['duration']:.2f} seconds"
    )

    print(
        f"Packets/Second   : "
        f"{stats['pps']:.2f}"
    )

    print(
        f"Bytes/Second     : "
        f"{stats['bps']:.2f}"
    )    
