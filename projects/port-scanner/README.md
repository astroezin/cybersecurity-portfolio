# Python Port Scanner

A simple TCP port scanner written in Python using the built-in `socket` library.

## Features

- Scan one or more TCP ports
- Fast timeout (1 second)
- Simple command-line interface
- Detects open and closed ports
- Beginner-friendly source code

## Requirements

- Python 3

## Usage

```bash
python3 scanner.py <host> <port1> [port2 port3 ...]
```

### Example

```bash
python3 scanner.py scanme.nmap.org 22 80 443
```

### Sample Output

```text
========================================
Scanning scanme.nmap.org
========================================
[+] Port 22 is OPEN
[+] Port 80 is OPEN
[-] Port 443 is CLOSED
```

## Disclaimer

This tool is intended for educational purposes and for scanning systems you own or have permission to test.
