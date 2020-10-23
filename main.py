import os
import sys

ciphertext_1_file = open("challenge1.txt", "rb")
ciphertext_2_file = open("challenge2.txt", "rb")

byte = ciphertext_1_file.read(1)
ciphertext_1_bytes = []
while byte:
    ciphertext_1_bytes.append(byte)
    byte = ciphertext_1_file.read(1)

print(f"Ciphertext 1 contains {len(ciphertext_1_bytes)} bytes:")
for index, b in enumerate(ciphertext_1_bytes):
    print(f"{index}: {b}")

print("\n\n--------------------------------")

byte2 = ciphertext_2_file.read(1)
ciphertext_2_bytes = []
while byte2:
    ciphertext_2_bytes.append(byte2)
    byte2 = ciphertext_2_file.read(1)

print(f"Ciphertext 2 contains {len(ciphertext_2_bytes)} bytes:")
for index, b in enumerate(ciphertext_2_bytes):
    print(f"{index}: {b}")
