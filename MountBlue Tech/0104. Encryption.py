#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    n = len(s)
    col = math.ceil(math.sqrt(n))
    row = math.floor(math.sqrt(n))
    
    if row* col < n:
        row +=1
    res = []
    li = []
    for i in range(col):
        chars = ''
        for j in range(row):
            if i+j*col<n:
                chars += s[i+j*col]
        li.append(chars)
    return " ".join(li)   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
