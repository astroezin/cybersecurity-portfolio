# Subnetting

Subnetting divides a large network into smaller, more manageable networks (subnets). It improves network organization, performance, and security.

---

## IPv4 Address

An IPv4 address consists of **32 bits** divided into four octets.

Example:

```text
192.168.1.10
```

Binary representation:

```text
11000000.10101000.00000001.00001010
```

---

## CIDR Notation

CIDR (Classless Inter-Domain Routing) specifies the network prefix.

| CIDR | Subnet Mask | Hosts |
|------|-------------|------:|
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /29 | 255.255.255.248 | 6 |
| /30 | 255.255.255.252 | 2 |

---

## Example

Network:

```text
192.168.1.0/24
```

Network Address:

```text
192.168.1.0
```

Broadcast Address:

```text
192.168.1.255
```

Usable Hosts:

```text
192.168.1.1 - 192.168.1.254
```

---

## Private IPv4 Ranges

| Range | CIDR |
|--------|------|
| 10.0.0.0 | /8 |
| 172.16.0.0 - 172.31.255.255 | /12 |
| 192.168.0.0 | /16 |

---

## Why Subnet?

- Improve performance
- Reduce broadcast traffic
- Increase security
- Better network management
