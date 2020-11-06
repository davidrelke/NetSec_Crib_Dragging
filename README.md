# One-Time Pad Crib Dragging

## Instructions
Created with Python 3.8, previous versions might also work. No externel libraries are needed.

Two executable scripts are provided: main.py and helper.py.

### The Helper
This utility can be used to search the extensive list of englisch words taken from [here](https://github.com/dwyl/english-words). It can search for words starting with, containing or ending with a given string.
Run `python helper.py` to see examples ofthe syntax used.
Entering `erties*` for example will search for all words ending with the string 'erties':
```
Enter your string:
erties*
Search for words that end with 'erties''
champerties
interties
liberties
poverties
properties
puberties
Saugerties
uberties
-------------------------------------
```
This tool can be used to find words that match fragments revealed during the crib-dragging process.

### The Crib-Dragging Script
Run `python main.py challenge1.txt challenge2.txt`. This script will read both ciphertexts and guide the user trough a crib-dragging analysis of the encrypted messages.