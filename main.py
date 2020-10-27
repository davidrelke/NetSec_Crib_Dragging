import array
import csv
import os
import sys
from collections import defaultdict
import enchant
import re

from typing import List

enchant_dictionary = enchant.Dict("en_US")

def byte_xor(ba1, ba2) -> List[int]:
    res: List[int] = []
    [res.append(_a ^ _b) for _a, _b in zip(ba1, ba2)]
    return res


def check_ascii_code_allowed(ascii_codes: List[int]) -> bool:
    for c in ascii_codes:
        if c not in allowed_ascii_codes:
            return False

    return True


ciphertext_1_file = open("challenge1.txt", "rb")
ciphertext_2_file = open("challenge2.txt", "rb")

byte: bytes = ciphertext_1_file.read(1)
ciphertext_1_bytes: List[int] = []
while byte:
    ciphertext_1_bytes.append(int.from_bytes(byte, 'little'))
    byte = ciphertext_1_file.read(1)

print(f"Ciphertext 1 contains {len(ciphertext_1_bytes)} bytes")
# [print(f"{index}: {value} - {hex(value)}") for index, value in enumerate(ciphertext_1_bytes)]

print("--------------------------------")

byte2 = ciphertext_2_file.read(1)
ciphertext_2_bytes: List[int] = []
while byte2:
    ciphertext_2_bytes.append(int.from_bytes(byte2, 'little'))
    byte2 = ciphertext_2_file.read(1)

print(f"Ciphertext 2 contains {len(ciphertext_2_bytes)} bytes")
# [print(f"{index}: {value} - {hex(value)}") for index, value in enumerate(ciphertext_2_bytes)]

print("--------------------------------")

ciphertext_xor: List[int] = []

for i in range(len(ciphertext_2_bytes)):
    # ciphertext_xor.append(int.from_bytes(byte_xor(ciphertext_1_bytes[i], ciphertext_2_bytes[i]), 'little'))
    ciphertext_xor.append(ciphertext_1_bytes[i] ^ ciphertext_2_bytes[i])


print(f"XOR of c1 and c2 contains {len(ciphertext_xor)} bytes")
# [print(f"{i}:{d}") for i, d in enumerate(ciphertext_xor)]
print("--------------------------------")


allowed_ascii_codes: List[int] = list(range(32, 48)) + list(range(58, 127))
possible_words: List[str] = []


# with open('FrequentEnglishWordList.csv', 'r') as f:
#     reader = csv.reader(f)
#     crib_list = list(reader)
# # Remove the header of the list file
# crib_list = crib_list[1:]
#
# for index, crib in enumerate(crib_list):
#     crib_bytes: List[int] = []
#     crib_word = crib[1].capitalize()
#     [crib_bytes.append(int.from_bytes(c.encode('ascii'), 'little')) for c in crib_word]
#     local_result = byte_xor(ciphertext_xor[0:len(crib_bytes)], crib_bytes)
#
#     if not check_ascii_code_allowed(local_result):
#         continue
#
#     local_result_text: str = ""
#     for c in local_result:
#         local_result_text += chr(c)
#
#     if not local_result_text[0].isupper():
#         continue
#
#     if re.search(r'[^A-Za-z0-9 ]+', local_result_text):
#         continue
#
#     possible_words.append(local_result_text)
#
#     print(f"{index}:{crib_word} - {local_result_text}")
        
        
# Using readlines()
# file1 = open('words.txt', 'r')
# all_words = file1.readlines()
#
#
#
#
#
guess_word: str = """Taken in its entirety, the Snowden archive led to an ultimately simple conclusion: the U.S. government had built a system that has as its goal the complete elimination of electronic privacy worldwide."""
# Something interesting found so far:
# "would the jon"
# "I do " and "Talk " at [0]
# [81] "conclusion: the U.S. government had built a system that has as its goal the complete elimination of electronic privacy worldwide" =>
#      "I can't in good conscience allow the U.S. government to destroy privacy, internet freedom and basic liberties for people around the world with this massive surveillance machine they're secretly build"ing
guess_word_bytes: List[int] = []
[guess_word_bytes.append(int.from_bytes(c.encode('ascii'), 'little')) for c in guess_word]
possible_words: List[str] = []


# print(f"Guess word is '{guess_word}'")
# r = enchant_dictionary.check(guess_word)
# sug = enchant_dictionary.suggest("uld")


for i in range(len(ciphertext_xor) - len(guess_word)):
    local_result = byte_xor(ciphertext_xor[i:i+len(guess_word)], guess_word_bytes)
    local_result_text: str = ""

    if not check_ascii_code_allowed(local_result):
        continue

    for c in local_result:
        local_result_text += chr(c)

    possible_words.append(local_result_text)
    # print(f"At {i}: {local_result} = {local_result_text}")
    print(f"At {i}:--{local_result_text}--")

print(f"Found {len(possible_words)} possible words")
#
#
#
#
#
#
#


















# precalculated_ascii_xor: defaultdict = defaultdict()
# for ascii_code_1 in allowed_ascii_codes:
#     for ascii_code_2 in allowed_ascii_codes:
#         xor = ascii_code_1 ^ ascii_code_2
#         if xor not in precalculated_ascii_xor:
#             precalculated_ascii_xor[xor] = []
#         precalculated_ascii_xor[xor].append((ascii_code_1, ascii_code_2))
#
# print(len(precalculated_ascii_xor))
#
# res: defaultdict = defaultdict()
#
#
# for index, letter in enumerate(ciphertext_xor):
#     res[index] = possible = precalculated_ascii_xor.get(letter)
#
# sol1: List[str] = []
# sol2: List[str] = []
#
# s = []
# for index in res:
#     if index > 10:
#         break
#
#     s.append(res[index])
#
#
#
# c1 = ""
# for b in ciphertext_1_bytes:
#     c1 += hex(b).replace("0x", "")
#
# c2 = ""
# for b in ciphertext_2_bytes:
#     c2 += hex(b).replace("0x", "")
#
# print("wololol")