# Bash Cheat Sheet

## File and Directory Commands

```bash
pwd
ls
ls -la
cd
mkdir
rmdir
rm
rm -rf
cp
mv
touch
cat
less
head
tail
find
locate
```

## Search

```bash
grep "text" file.txt
grep -r "password" .
```

## File Permissions

```bash
chmod +x file.sh
chmod 755 file
chmod 644 file
chown user:user file
```

## Compression

```bash
zip archive.zip file
unzip archive.zip
tar -czvf archive.tar.gz folder
tar -xzvf archive.tar.gz
```

## Networking

```bash
ping google.com
curl https://example.com
wget https://example.com/file
netstat -tuln
ss -tuln
```

## Processes

```bash
ps aux
top
htop
kill PID
kill -9 PID
```

## Disk Usage

```bash
df -h
du -sh *
```

## Users

```bash
whoami
id
sudo
passwd
```

## System Information

```bash
uname -a
hostname
uptime
free -h
lscpu
```
