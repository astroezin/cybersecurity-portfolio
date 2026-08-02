# Linux Package Management

Package managers allow you to install, update, and remove software efficiently.

---

## Debian / Ubuntu / Kali (APT)

### Update package list

```bash
sudo apt update
```

### Upgrade installed packages

```bash
sudo apt upgrade
```

### Install a package

```bash
sudo apt install nmap
```

### Remove a package

```bash
sudo apt remove nmap
```

### Remove package and configuration

```bash
sudo apt purge nmap
```

### Remove unused packages

```bash
sudo apt autoremove
```

### Search for a package

```bash
apt search wireshark
```

### Show package information

```bash
apt show python3
```

---

## Red Hat / Fedora (DNF)

Install

```bash
sudo dnf install nmap
```

Update

```bash
sudo dnf update
```

Remove

```bash
sudo dnf remove nmap
```

---

## Arch Linux (Pacman)

Install

```bash
sudo pacman -S nmap
```

Update

```bash
sudo pacman -Syu
```

Remove

```bash
sudo pacman -R nmap
```

---

## Python Packages

Install

```bash
pip install requests
```

Install from requirements

```bash
pip install -r requirements.txt
```

List installed packages

```bash
pip list
```

Freeze dependencies

```bash
pip freeze > requirements.txt
```

---

## Best Practices

- Update package lists before installing new software.
- Install software only from trusted repositories.
- Remove unused packages regularly.
- Keep systems updated with security patches.
