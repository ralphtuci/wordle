#3/1/2022
#ralph tran

import requests
import random
import collections

# make the list of words from txt file on github
def makelist():
    word_site = "https://raw.githubusercontent.com/ralphtuci/wordle/main/wordle-full-list.txt"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    return WORDS

# check for duplicate letters
def checkdupe(CHOICE):
    d = collections.defaultdict(int)
    for c in CHOICE:
        d[c] += 1
    for c in d:
        if (d.get(c) > 1):
            return True
    return False
        
# check for certain consonants STRLN
def checkcons(CHOICE):
    for c in CHOICE:
        if (c == 's' or c == 't' or c == 'r' or c == 'l' or c == 'n'):
            return False
    return True

# check for number of vowels
def checkvow(CHOICE):
    vow = 0
    for c in CHOICE:
        if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
            vow += 1
        if (vow > 1):
            return True
    return False

# get specific word depending on choice
def getword(switch, WORDS):
    CHOICE = bytes.decode(random.choice(WORDS))
    # easy
    if   (switch == 1):
        while (1):
            if checkdupe(CHOICE):
                pass
            else:
                if checkcons(CHOICE):
                    pass
                else:
                    if checkvow(CHOICE):
                        break
            CHOICE = bytes.decode(random.choice(WORDS))
    # normal
    elif (switch == 2):
        pass
    # hard
    elif (switch == 3):
        while (1):
            if checkdupe(CHOICE):
                break
            else:
                pass  
            CHOICE = bytes.decode(random.choice(WORDS))
    else:
        print ("Incorrect choice. This should never show up, but if it does, I just want to let you know you're a complete failure.")
    return CHOICE