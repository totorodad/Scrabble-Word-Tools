# scrab.py
# Various Scrabble dictionary filters
# 
# scrab <cmd> <text>
# cmd's:
#   sw: search words that begin with
#   ew: search words that end with
#   ci: search words that are contained in
#   us: unscramble letters into words
#	an: anagram generator

# # Reference Webpage:
# https://code.visualstudio.com/docs/python/python-tutorial
# 
from ctypes.wintypes import CHAR
from sys import argv

import numpy as np

# Standard Scrabble tile face value worth: A=1, B=3 ect.
worth = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]

def word_worth (s):
    ww=0
    for xx in range (0, len(s)):
        ww = ww + worth[ord(s[xx]) - ord ('A')]
    return (ww)

if len (argv) != 3:
    print("SCRAB Verison 1.0, J. Nolan 26-Nov-2022")
    print("Usage: " + argv[0] + " <cmd> " + " <text>")
    exit(1)

script, cmd, text = argv

if (cmd != "sw" and cmd != "ew" and cmd != "ci" and cmd != "us" and cmd != "an"):
    print("Supported commands are:")
    print("--------------------------------------------------------")
    print("sw: starts with")
    print("ew: ends with")
    print("ci: contained in.  This can include prefix and suffix")
    print("us: Unscramble letters into valid scrabble words")
    print("an: Anagrams")
    exit(1)

#read in the scrabble dictionary words
File_data = np.loadtxt("Collins Scrabble Words (2019).txt", skiprows=1, dtype="str")
s = text.upper()
count = 0

if (cmd == "sw"):
    for each in File_data:
        if each[:len(s)] == s:
            print("Found word-prefix: " + each + " (" + str(word_worth(each)) + ")")
            count = count + 1
    if count == 0:
        print("Sorry")
    else:
        print("Found " + str(count) + " words")
        print("Done")

if (cmd == "ew"):
    for each in File_data:
        if each[len(s):] == s:
            print("Found word-suffix: " + each + " (" + str(word_worth(each)) + ")")
            count = count + 1
    if count == 0:
        print("Sorry")
    else:
        print("Found " + str(count) + " words")
        print("Done")

if (cmd == "ci"):
    for each in File_data:
        if each.find(s) > 0:
            print("Found in word: " + each + " (" + str(word_worth(each)) + ")")
            count = count + 1
    if count == 0:
        print("Sorry")
    else:
        print("Found " + str(count) + " words")
        print("Done")


if (cmd == "us"):
    print ("Unscramballing: " + s)

    for each in File_data:
        search_word = each
        for x in range (0, len(each)):
            for y in range(0, len(s)):
                # build the word from the s letters if possible
                if each[x] == s[y]:
                    count = count + 1
                    s = s[:y]+"*"+s[y+1:] # erase the used char
                    each = each[:x]+"-"+each[x+1:] # erase the used char
        if (count == len(each)):
            each = search_word # restore the value of the search word
            print("Found: " + each + " (" + str(word_worth(each)) + ")")
        count = 0
        s = text.upper() # restore source word
    print ("done")

if (cmd == "an"):
    print ("Anagrams of: " + s)

    for each in File_data:
        search_word = each
        for x in range (0, len(each)):
            for y in range(0, len(s)):
                # build the word from the s letters if possible
                if each[x] == s[y]:
                    count = count + 1
                    s = s[:y]+"*"+s[y+1:] # erase the used char
                    each = each[:x]+"-"+each[x+1:] # erase the used char
        if (count == len(each)== len(s)):
            each = search_word # restore the value of the search word
            s=text.upper() # restore S
            if (each != s):
                print("Found: " + each + " (" + str(word_worth(each)) + ")")
        count = 0
        s = text.upper() # restore source word
    print ("done")