#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    cipher = ""
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                n = ((ord(s[i]) + k) - 97) % 26
                n += 97
            else:
                n = ((ord(s[i]) + k) - 65) % 26
                n += 65
            cipher += chr(n)
        else:
            cipher += s[i]
    return cipher
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
