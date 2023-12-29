# starts_with.py
# Returns all scrabble words from the Collins Scrabble dictionary that start with the argv letters

# # Reference Webpage:
# https://code.visualstudio.com/docs/python/python-tutorial
# 
from ctypes.wintypes import CHAR
from sys import argv

import numpy as np

script, firstargument = argv

#read in the scrabble dictionary words
File_data = np.loadtxt("Collins Scrabble Words (2019).txt", skiprows=1, dtype="str")
s = firstargument.upper();
count = 0

for each in File_data:
    if each[:len(s)] == s:
        print("Found word: " + each)
        count=count+1
if count == 0:
    print("Sorry")
else:
    print("Found " + str(count) + " words")
    print("Done")
