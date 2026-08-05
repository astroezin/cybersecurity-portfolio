# PCAP Analyzer

A professional Python-based network traffic analysis tool that reads PCAP files and extracts useful security and forensic information.

The project is designed to help security analysts understand network traffic by analyzing protocols, IP addresses, conversations, ports, packet sizes, and capture statistics.

Built as part of a Cybersecurity Portfolio focused on SOC analysis, network security, and defensive security engineering.

---

# Features

## PCAP Analysis

- Read and analyze PCAP capture files
- Count total packets
- Extract packet information using Scapy

## Protocol Analysis

- TCP traffic analysis
- UDP traffic analysis
- ICMP traffic analysis
- Non-IP packet detection
- Protocol distribution statistics

## IP Analysis

- Top source IP addresses
- Top destination IP addresses
- Network conversation tracking

## Port Analysis

- TCP destination port analysis
- UDP destination port analysis
- Automatic service name identification

Supported services include:

- HTTP
- HTTPS
- DNS
- SSH
- FTP
- SMTP
- SMB
- RDP
- and more

## Packet Statistics

Calculates:

- Total bytes
- Smallest packet
- Largest packet
- Average packet size

## Capture Statistics

Provides:

- Capture start time
- Capture end time
- Capture duration
- Packets per second
- Bytes per second

---

# Technologies Used

- Python 3
- Scapy
- Linux / Kali Linux
- Git & GitHub
- Command Line Interface (CLI)

---

# Installation

## Clone Repository

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
