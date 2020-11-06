# One-Time Pad Crib Dragging

## Result

The two messages are quotes taken from the book "No Place to Hide" by Glenn Greenwald and the [article](https://www.theguardian.com/world/2013/jun/09/edward-snowden-nsa-whistleblower-surveillance) "Edward Snowden: the whistleblower behind the NSA surveillance revelations" authored by Glenn Greenwald, Ewen MacAskill and Laura Poitras.
> Taken in its entirety, the Snowden archive led to an ultimately simple conclusion: the U.S. government had built a system that has as its goal the complete elimination of electronic privacy worldwide.

>I can't in good conscience allow the U.S. government to destroy privacy, internet freedom and basic liberties for people around the world with this massive surveillance machine they're secretly building.

The Key is:
```
4a9fbf3cf9dc67aa6eb9628e4bb4c8ba5d1577d9f36271c7c3b7ed9ad2aebd9b99947f7059d368b9ca94c94922d25e461f18c8e788d7c9c931926176d333ca773cc889f57e93d6af38a4d8493f91054346f3a6736bf0a7ad2a86911ab24ed8324e34539eaa6574a8956bb2a6be7bae05acba136beb974e6142dcdfa75f4bcbdc19a9ef4876cbae0fc2a36a432799bc2c77a4478e2a48e44573e412b51267af4e933eaec76caed5fd1b46289bbd4d8e2c875b9be22c5be6899240c061937bac096657902c7
```

## Approach
The messages _m1_ and _m2_ have been encrypted using the same key _k_.We have the two corresponding ciphertexts _c1_ and _c2_. These were encrypted by computing the bitwise exclusive or of each message with the key:  
_c1_ = _m1_ ⊕ _k_  
_c2_ = _m2_ ⊕ _k_  
The reuse of k introduces a [vulnerability](https://www.thecrowned.org/the-one-time-pad-and-the-many-time-pad-vulnerability) to the otherwise secure OTP method.
We can compute  
_x_ = _c1_ ⊕ _c2_ = _m1_ ⊕ _k_ ⊕ _m2_ ⊕ _k_ = _m1_ ⊕ _m2_.  
This reveals information about the two plaintext messages and the key.  
The tool enables the user to mount a [crib-dragging](http://www.ivansivak.net/blog/stream-ciphers-one-time-pad-and-the-same-key-vs-cbc) attack against _x_. The user enters a string that might be in one (or both) of the two original messages. This guessed string _g_ is than 'dragged' over _x_ by computing
_x_ ⊕ _g_ at all possible positions. If _g_ actually existed in one of the messages we will get the plaintext of the other message at the corresponding positions.  
This way the user can gradually restore the original messages.  
After the messages are recovered the key can be computed:  
_c1_ ⊕ _m1_ = _k_

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
The script takes only the following characters and the whitespace into account: 
```
 ',.:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
 ```
 That way it can filter out any implausible matches of the guessed word and c1 ⊕ _c2_.  
 Finding a starting point was the hardest part. Using very common but short words like 'the' as the first guess will lead to a lot of false positives. It therefor makes sense to use a longer (more than ~7 characters) word. Including whitespaces around the word will also narrow down the set of possible matches. 
 ### Example
 We used the string ' government ' (notice the leading and tailing whitespace to increase the length of the guessed string) as the first guess. This yields to only three results of which two look like plausible text fragments.

 ```
 Iteration 1: Guess is now ' government '
[41]--e led to an --
[59]-- plvequiccry--
[91]--nd basic lib--
Select one that looks plausible: 91
Iteration 1: You chose 'nd basic lib'
Belongs the guess word ' government ' to message [1] or [2]?
1
Iteration 1: Current message1:
########################################################################################### government #################################################################################################
Iteration 1: Current message2:
###########################################################################################nd basic lib#################################################################################################
 ```
 From there on we can guess that the revealed 'nd basic lib' might be ' and basic lib'. This way we reveal two more characters in the other message:  
 ```
 Iteration 2: Enter a string to guess below:
 and basic lib
Iteration 2: Guess is now ' and basic lib'
[89]--S. government --
Select one that looks plausible: 89
Iteration 2: You chose 'S. government '
Belongs the guess word ' and basic lib' to message [1] or [2]?
2
Iteration 2: Current message1:
#########################################################################################S. government #################################################################################################
Iteration 2: Current message2:
######################################################################################### and basic lib#################################################################################################
 ```
 We continue to either guess typical words or complete revealed fragments.
 The full console output of our first full decryption can be found [here](https://github.com/davidrelke/NetSec_Crib_Dragging/blob/master/console_output.txt).

