from typing import List
from signal import signal, SIGINT
from sys import exit
def handler(signal_received, frame):
    exit(0)
    
signal(SIGINT, handler)

wordlist_file = open('wordlist.txt', 'r')
all_words: List[str] = wordlist_file.readlines()
for i, word in enumerate(all_words):
    all_words[i] = word.replace('\n', '')
    
print(f"Crib-Drag Helper! This uses a list of the 10,000 most common english words to give some inspiration.")
print(f"Enter a string that you suspect to be a part of a word.")
print("Add a '*' before the string to search for words that start with this string.")
print("Add a '*' after the string to search for words that end with this string.")
print("Surround the string with '*' to search for words that start with, end with or contain this string.")
print("Examples:")
print("-------------------------------------")

word = "survei"
print(f"*{word}")

res = [w for w in all_words if w.startswith(word)]
[print(w) for w in res]

print("-------------------------------------")
word = "erties"
print(f"{word}*")
res = [w for w in all_words if w.endswith(word)]
[print(w) for w in res]

print("-------------------------------------")
word = "ovelt"
print(f"*{word}*")
res = [w for w in all_words if  word in w]
[print(w) for w in res]

print("-------------------------------------")
print("Press Ctrl + C to exit")

while True:
    print("-------------------------------------")
    input_string = input("Enter your string:\n")
    
    try:
        if not '*' in input_string:
            print("Input did not contain '*'")
            continue
        
        word = input_string.replace("*", "")
        if input_string.startswith('*') and input_string.endswith('*'):
            print(f"Search for words that contain '{word}'")
            res = [w for w in all_words if  word in w]
            [print(w) for w in res]
            
        elif input_string.startswith('*'):
            print(f"Search for words that start with '{word}''")
            res = [w for w in all_words if w.startswith(word)]
            [print(w) for w in res]
            
        elif input_string.endswith('*'):
            print(f"Search for words that end with '{word}''")
            res = [w for w in all_words if w.endswith(word)]
            [print(w) for w in res]
        
    except ValueError:
        print("Could not read input")