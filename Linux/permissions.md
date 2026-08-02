# Linux File Permissions

## Permission Format

Example:

```text
-rwxr-xr--
```

Meaning:

| Symbol | Description |
|---------|-------------|
| - | File |
| d | Directory |
| r | Read |
| w | Write |
| x | Execute |

## Permission Groups

Owner

Group

Others

Example

```text
rwx r-x r--
```

Owner:

- Read
- Write
- Execute

Group:

- Read
- Execute

Others:

- Read

## Numeric Permissions

| Number | Permission |
|---------|------------|
|7|rwx|
|6|rw-|
|5|r-x|
|4|r--|
|3|-wx|
|2|-w-|
|1|--x|
|0|---|

Examples

```bash
chmod 755 script.sh
chmod 644 notes.txt
chmod 600 secret.txt
```

## Change Owner

```bash
chown username file
```

## Change Group

```bash
chgrp developers file
```

## View Permissions

```bash
ls -l
```
