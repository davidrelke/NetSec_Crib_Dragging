# One-Time Pad Crib Dragging

## Result

The two messages are quotes taken from the book "No Place to Hide" by Glenn Greenwald and the [article](https://www.theguardian.com/world/2013/jun/09/edward-snowden-nsa-whistleblower-surveillance) "Edward Snowden: the whistleblower behind the NSA surveillance revelations" authored by Glenn Greenwald, Ewen MacAskill and Laura Poitras.
> Taken in its entirety, the Snowden archive led to an ultimately simple conclusion: the U.S. government had built a system that has as its goal the complete elimination of electronic privacy worldwide.

>I can't in good conscience allow the U.S. government to destroy privacy, internet freedom and basic liberties for people around the world with this massive surveillance machine they're secretly building

## Approach
The messages m1 and m2 have been encrypted using the same key k.We have the two corresponding ciphertexts c1 and c2. These were encrypted by computing the bitwise exclusive or of each message with the key:  
c1 = m1 ⊕ k  
c2 = m2 ⊕ k  
The reuse of k introduces a [vulnerability](https://www.thecrowned.org/the-one-time-pad-and-the-many-time-pad-vulnerability) to the otherwise secure OTP method.
We can compute  
x = c1 ⊕ c2 = m1 ⊕ k ⊕ m2 ⊕ k = m1 ⊕ m2.  
This reveals information about the two plaintext messages and the key.  
The tool enables the user to mount a [crib-dragging](http://www.ivansivak.net/blog/stream-ciphers-one-time-pad-and-the-same-key-vs-cbc) attack against x. The user enters a string that might be in one (or both) of the two original messages. This guessed string g is than 'dragged' over x by computing
x ⊕ g at all possible positions. If g actually existed in one of the messages we will get the plaintext of the other message at the corresponding positions.  
This way the user can gradually restore the original messages.

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
Run `python main.py challenge1.txt challenge2.txt`. This script will read both ciphertexts and guide the user trough a crib-dragging analysis of the encrypted messages. Each step is saved in the output.txt file which includes the (partly) decrypted messages and the key.