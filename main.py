import array
import csv
import os
import sys
from collections import defaultdict
import re
from iteration_message import IterationMessage
from typing import List, Dict


def byte_xor(ba1, ba2) -> List[int]:
    res: List[int] = []
    [res.append(_a ^ _b) for _a, _b in zip(ba1, ba2)]
    return res

def check_ascii_code_allowed(ascii_codes: List[int]) -> bool:
    for c in ascii_codes:
        if c not in allowed_ascii_codes:
            return False

    return True

def crib_drag(guess_word_bytes: List[int]) -> Dict[int, str]:
    possible_words: Dict[int,str] = dict()
    for i in range(len(ciphertext_xor) - len(guess_word_bytes) + 1):
        local_result = byte_xor(ciphertext_xor[i:i+len(guess_word_bytes)], guess_word_bytes)
        local_result_text: str = ""
        if not check_ascii_code_allowed(local_result):
            continue
        for c in local_result:
            local_result_text += chr(c)
        possible_words[i] = local_result_text
    
    return possible_words

def print_current_messages(msg1:List[str], msg2:List[str], iter: int) -> None:
    print(f"Iteration {iter}: Current message1:")
    msg_1_str = ''.join(msg1)
    print(msg_1_str)
    print(f"Iteration {iter}: Current message2:")
    msg_2_str = ''.join(msg2)
    print(msg_2_str)

def undo_iteration(iter_msgs: List[IterationMessage], iter: int) -> int:
    print(f"Undoing the last iteration.")
    if len(iter_msgs) > 1:
        msg1 = iter_msgs[len(iter_msgs) - 2].message_1
        msg2 = iter_msgs[len(iter_msgs) - 2].message_2
        iter_msgs.pop()
        iter -= 2

    print_current_messages(msg1, msg2, iter)
    return iter


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


allowed_ascii_codes: List[int] = [32, 39, 44, 46, 58] + list(range(65, 91)) + list(range(97, 123))
#                                " " "'" "," "." ":"
allowed_chars = []
[allowed_chars.append(chr(c)) for c in allowed_ascii_codes]

iteration = 0
iteration_messages: List[IterationMessage] = []
l1 = ['#'] * len(ciphertext_xor)
l2 = l1.copy()
iteration_messages.append(IterationMessage(l1, l2, iteration))

print("These characters are allowed:")
print("".join(allowed_chars))

print("Enter your first guess (including punctuation and whitespace). This string will be dragged over the XOR of both ciphertexts. Tip: start with ' government '!")

# "Taken in its entirety, the Snowden archive led to an ultimately simple conclusion: the U.S. government had built a system that has as its goal the complete elimination of electronic privacy worldwide."
# "I can't in good conscience allow the U.S. government to destroy privacy, internet freedom and basic liberties for people around the world with this massive surveillance machine they're secretly buildi"(ng)


while True:
    iteration += 1
    
    guess_word: str = input(f"Iteration {iteration}: Enter a string to guess below:\n")
    if guess_word == "":
        print("Enter a valid string")
        iteration -= 1
        continue
    
    if guess_word == "*back*":
        iteration = undo_iteration(iteration_messages, iteration)
        continue
        
        
    print(f"Iteration {iteration}: Guess is now '{guess_word}'")


    guess_word_bytes: List[int] = []
    [guess_word_bytes.append(int.from_bytes(c.encode('ascii'), 'little')) for c in guess_word]
    possible_words: Dict[int,str] = crib_drag(guess_word_bytes)
        

    if len(possible_words) == 0:
        print("Iteration {iteration}: Could not find any match. Try with another string.")
        iteration -= 1
        continue
    
    
    for i in possible_words:
        print(f"[{i}]--{possible_words[i]}--")
    
    
    selected_position = input("Select one that looks plausible: ")
    if guess_word == "*back*":
        iteration = undo_iteration(iteration_messages, iteration)
        continue
        
    
    try:
        selected_position = int(selected_position)
        if selected_position not in possible_words:
            print(f"Please enter a valid position")
            
        else:
            selected_word = possible_words[selected_position]
            word_length = len(selected_word)
            
            print(f"Iteration {iteration}: You chose '{selected_word}'")
            
            
            selected_word_list = []
            [selected_word_list.append(c) for c in selected_word]
            guess_word_list = []
            [guess_word_list.append(c) for c in guess_word]
            
            guess_belongs_to = 1
            if len(iteration_messages) != 0:
                guess_belongs_to = input(f"Belongs the guess word '{guess_word}' to message [1] or [2]?\n")
                if guess_word == "*back*":
                    iteration = undo_iteration(iteration_messages, iteration)
                    continue
            
            iteration_messages.append(IterationMessage(iteration_messages[iteration - 1].message_1.copy(), iteration_messages[iteration - 1].message_2.copy(), iteration))
            if guess_belongs_to == '1':
                iteration_messages[iteration].message_2[selected_position:selected_position+word_length] = selected_word_list
                iteration_messages[iteration].message_1[selected_position:selected_position+word_length] = guess_word_list
            else:
                iteration_messages[iteration].message_1[selected_position:selected_position+word_length] = selected_word_list
                iteration_messages[iteration].message_2[selected_position:selected_position+word_length] = guess_word_list
            
            
            print_current_messages(iteration_messages[iteration].message_1, iteration_messages[iteration].message_2, iteration)
    except ValueError:
        print("Please enter an int")
        