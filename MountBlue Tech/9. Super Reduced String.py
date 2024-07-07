#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    li = []
    li.append(s[0])
    for i in range(1,len(s)):
        if li:
            if s[i] == li[-1]:
                li.pop()
            else:
                li.append(s[i])
        else:
            li.append(s[i])
    return "".join(li) if li else "Empty String"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
