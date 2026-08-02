# TCP/IP Model

The TCP/IP model is the practical networking model used on the Internet.

| Layer | Protocols |
|--------|-----------|
| Application | HTTP, HTTPS, DNS, FTP, SMTP |
| Transport | TCP, UDP |
| Internet | IP, ICMP |
| Network Access | Ethernet, Wi-Fi |

---

## TCP

Transmission Control Protocol

Features:

- Reliable
- Connection-oriented
- Error checking
- Ordered delivery

Examples:

- HTTP
- HTTPS
- SSH
- FTP

---

## UDP

User Datagram Protocol

Features:

- Fast
- Connectionless
- No guaranteed delivery

Examples:

- DNS
- VoIP
- Streaming
- Online gaming

---

## IP

Internet Protocol

Responsible for:

- Addressing
- Routing
- Packet delivery

Versions:

- IPv4
- IPv6

---

## ICMP

Internet Control Message Protocol

Used for:

- Error reporting
- Network diagnostics

Commands:

```bash
ping
traceroute
```

---

## TCP Three-Way Handshake

```
Client        Server

SYN -------->

<-------- SYN ACK

ACK -------->
```

This establishes a reliable TCP connection before data is exchanged.
