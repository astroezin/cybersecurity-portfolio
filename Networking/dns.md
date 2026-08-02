# Domain Name System (DNS)

DNS translates human-readable domain names into IP addresses.

Example:

```text
google.com → 142.250.x.x
```

---

## Common DNS Record Types

| Record | Purpose |
|---------|----------|
| A | IPv4 Address |
| AAAA | IPv6 Address |
| CNAME | Alias |
| MX | Mail Server |
| NS | Name Server |
| TXT | Text Information |
| PTR | Reverse DNS |
| SOA | Start of Authority |

---

## Useful Commands

Lookup

```bash
nslookup google.com
```

Detailed lookup

```bash
dig google.com
```

Reverse lookup

```bash
dig -x 8.8.8.8
```

Using host

```bash
host openai.com
```

---

## DNS Resolution Process

1. User enters a domain.
2. Browser checks cache.
3. Operating system checks cache.
4. Recursive resolver is queried.
5. Root server is contacted.
6. TLD server is queried.
7. Authoritative server responds.
8. IP address is returned.

---

## Security Concerns

- DNS Spoofing
- Cache Poisoning
- DNS Amplification
- DNS Tunneling

DNS is a common target in cyber attacks because nearly all internet communication depends on it.
