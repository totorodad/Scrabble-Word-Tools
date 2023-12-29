# Reference Webpage:
# https://code.visualstudio.com/docs/python/python-tutorial
# 
from ctypes.wintypes import CHAR
from sys import argv

import numpy as np

script, firstargument = argv

#read in the scrabble dictionary words
File_data = np.loadtxt("Collins Scrabble Words (2019).txt", skiprows=1, dtype="str")

for each in File_data:
    if each == firstargument.upper():
        print("Found word: " + each)
        exit()
print("Sorry!")
