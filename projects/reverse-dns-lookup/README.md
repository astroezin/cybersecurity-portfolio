# Reverse DNS Lookup Tool

A Python command-line tool that performs reverse DNS (PTR) lookups for IPv4 and IPv6 addresses.

---

## Features

- Reverse DNS (PTR) lookup
- Supports IPv4 and IPv6
- Validates IP addresses before lookup
- Displays hostname, aliases, and resolved addresses
- Built using Python's standard library

---

## Technologies Used

- Python 3
- socket
- ipaddress
- argparse

---

## Installation

```bash
git clone https://github.com/astroezin/cybersecurity-portfolio.git
cd cybersecurity-portfolio/projects/reverse-dns-lookup
```

No external dependencies are required.

---

## Usage

```bash
python3 reverse_dns.py 8.8.8.8
```

```bash
python3 reverse_dns.py 1.1.1.1
```

```bash
python3 reverse_dns.py 20.205.243.166
```

---

## Example Output

```text
============================================================
Reverse DNS Lookup
============================================================

IP Address : 8.8.8.8
Hostname   : dns.google
Aliases    : None
Addresses  : 8.8.8.8
```

---

## Skills Demonstrated

- DNS Fundamentals
- PTR Records
- Python Networking
- IP Address Validation
- Error Handling
- Command-Line Interfaces

---

## Interview Questions

### What is a PTR record?

A PTR (Pointer) record maps an IP address back to a hostname.

### Why is reverse DNS useful?

It helps identify systems behind IP addresses and is commonly used in email security, network administration, and incident response.

### Does every IP address have a PTR record?

No. Many IP addresses do not have reverse DNS configured.

---

## Future Improvements

- Bulk IP lookup from a file
- JSON output
- CSV export
- Concurrent lookups
- Lookup timing statistics
- Reverse DNS report generation

---

## Disclaimer

This project is intended for educational purposes and authorized security research only.
