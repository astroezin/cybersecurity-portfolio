#!/usr/bin/env python3

import argparse
import getpass
import hashlib
from pathlib import Path

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

SALT_SIZE = 16
KEY_SIZE = 32      # AES-256
NONCE_SIZE = 16
PBKDF2_ROUNDS = 200000


def derive_key(password: str, salt: bytes) -> bytes:
    return PBKDF2(password, salt, dkLen=KEY_SIZE, count=PBKDF2_ROUNDS)


def sha256_file(filename):
    h = hashlib.sha256()

    with open(filename, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()


def encrypt_file(filename):

    password = getpass.getpass("Password: ")

    salt = get_random_bytes(SALT_SIZE)
    key = derive_key(password, salt)

    cipher = AES.new(key, AES.MODE_GCM)

    with open(filename, "rb") as f:
        plaintext = f.read()

    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    output = filename + ".enc"

    with open(output, "wb") as f:
        f.write(salt)
        f.write(cipher.nonce)
        f.write(tag)
        f.write(ciphertext)

    print("=" * 55)
    print("Encryption Complete")
    print("=" * 55)
    print("Output :", output)
    print("SHA256 :", sha256_file(output))


def decrypt_file(filename):

    password = getpass.getpass("Password: ")

    with open(filename, "rb") as f:
        salt = f.read(SALT_SIZE)
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    key = derive_key(password, salt)

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    output = filename.replace(".enc", ".dec")

    with open(output, "wb") as f:
        f.write(plaintext)

    print("=" * 55)
    print("Decryption Complete")
    print("=" * 55)
    print("Output :", output)
    print("SHA256 :", sha256_file(output))


def main():

    parser = argparse.ArgumentParser(
        description="AES-256 File Encryptor"
    )

    parser.add_argument(
        "mode",
        choices=["encrypt", "decrypt"]
    )

    parser.add_argument(
        "file"
    )

    args = parser.parse_args()

    if not Path(args.file).exists():
        print("File not found.")
        return

    try:

        if args.mode == "encrypt":
            encrypt_file(args.file)

        else:
            decrypt_file(args.file)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
