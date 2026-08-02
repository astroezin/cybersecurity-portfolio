# Linux Networking Commands

## View IP Address

```bash
ip addr
hostname -I
```

## Routing

```bash
ip route
route -n
```

## DNS

```bash
cat /etc/resolv.conf
```

## Test Connectivity

```bash
ping google.com
```

## DNS Lookup

```bash
nslookup google.com
dig google.com
host google.com
```

## Check Listening Ports

```bash
ss -tuln
netstat -tuln
```

## Active Connections

```bash
ss -ant
```

## Download Files

```bash
wget URL
curl URL
```

## Interface Information

```bash
ip link
```

## MAC Address

```bash
ip link show
```
