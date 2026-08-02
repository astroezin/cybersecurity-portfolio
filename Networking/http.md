# HTTP and HTTPS

HTTP (Hypertext Transfer Protocol) is used to transfer web pages and data between clients and servers.

HTTPS is HTTP secured with TLS encryption.

---

## Common Ports

| Protocol | Port |
|-----------|------|
| HTTP | 80 |
| HTTPS | 443 |

---

## Common HTTP Methods

| Method | Purpose |
|----------|----------|
| GET | Retrieve data |
| POST | Submit data |
| PUT | Update data |
| DELETE | Remove data |
| PATCH | Partial update |
| HEAD | Headers only |
| OPTIONS | Supported methods |

---

## Common Status Codes

### Success

| Code | Meaning |
|------|----------|
|200|OK|
|201|Created|
|204|No Content|

### Redirect

| Code | Meaning |
|------|----------|
|301|Moved Permanently|
|302|Found|

### Client Errors

| Code | Meaning |
|------|----------|
|400|Bad Request|
|401|Unauthorized|
|403|Forbidden|
|404|Not Found|

### Server Errors

| Code | Meaning |
|------|----------|
|500|Internal Server Error|
|502|Bad Gateway|
|503|Service Unavailable|

---

## Common Security Headers

- Content-Security-Policy
- X-Frame-Options
- X-Content-Type-Options
- Strict-Transport-Security
- Referrer-Policy

---

## Common Attacks

- SQL Injection
- Cross-Site Scripting (XSS)
- CSRF
- Directory Traversal
- Remote File Inclusion
