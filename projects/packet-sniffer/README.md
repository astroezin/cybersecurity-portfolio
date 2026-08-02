# Packet Sniffer

A Python packet sniffer built with Scapy that captures live network traffic and displays basic packet information.

## Features

- Capture live packets
- Display source and destination IP addresses
- Detect TCP, UDP, and ICMP packets
- Show packet size
- Command-line interface with argparse
- Graceful shutdown with Ctrl+C

## Technologies Used

- Python 3
- Scapy

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Capture packets until interrupted:

```bash
sudo .venv/bin/python packet_sniffer.py
```

Capture a fixed number of packets:

```bash
sudo .venv/bin/python packet_sniffer.py --count 20
```

## Example Output

```text
Packet #1
Source IP      : 192.168.1.15
Destination IP : 8.8.8.8
Protocol       : UDP
Packet Length  : 74 bytes
```

## Project Structure

```text
packet-sniffer/
├── packet_sniffer.py
├── README.md
├── requirements.txt
├── .gitignore
└── screenshots/
```

## Skills Demonstrated

- Packet analysis
- Network protocols
- Python automation
- Scapy
- Command-line application development

## Future Improvements

- DNS packet parsing
- HTTP request detection
- Protocol filters
- Packet export to PCAP
- CSV logging
- Colored terminal output
- Interface selection
