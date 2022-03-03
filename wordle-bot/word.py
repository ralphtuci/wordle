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

def checkconz(CHOICE):
    for c in CHOICE:
        if (c == 'q' or c == 'w' or c == 'x' or c == 'v' or c == 'z'):
            return True
    return False

# check for number of vowels
def checkvow(CHOICE):
    vow = 0
    for c in CHOICE:
        if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
            vow += 1
        if (vow > 1):
            return True
    return False

def geteasy(words):
    while 1:
        choice = bytes.decode(random.choice(words))
        if checkdupe(choice):
            pass
        else:
            if checkcons(choice):
                pass
            else:
                if checkvow(choice):
                    break
    return choice


def getword(words):
    return bytes.decode(random.choice(words))


def gethard(words):
    while 1:
        choice = bytes.decode(random.choice(words))
        if checkdupe(choice):
            break
        else:
            pass
    return choice


def getex(words):
    while 1:
        choice = bytes.decode(random.choice(words))
        if checkdupe(choice):
            if checkconz(choice):
                break
            else:
                pass
    return choice
