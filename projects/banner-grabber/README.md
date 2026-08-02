# Banner Grabber

A simple Python TCP banner grabbing tool built using Python sockets.

## Features

- Connects to any TCP service
- Displays service banners
- Sends an HTTP HEAD request for web servers
- Configurable timeout
- Handles common network errors

## Requirements

- Python 3.10+

No external libraries are required.

## Usage

Single SSH banner:

```bash
python3 banner_grabber.py scanme.nmap.org 22
```

HTTP headers:

```bash
python3 banner_grabber.py scanme.nmap.org 80
```

Custom timeout:

```bash
python3 banner_grabber.py scanme.nmap.org 80 --timeout 5
```

## Example Output

SSH:

```
Banner from scanme.nmap.org:22

SSH-2.0-OpenSSH...
```

HTTP:

```
HTTP/1.1 200 OK
Server: nginx
...
```

## Skills Demonstrated

- Python
- TCP Networking
- Socket Programming
- Banner Grabbing
- Error Handling
- argparse

## Future Improvements

- Multi-threading
- TLS certificate detection
- Automatic service detection
- Save output to file
- JSON export
