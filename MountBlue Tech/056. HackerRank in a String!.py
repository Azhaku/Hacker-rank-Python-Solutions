#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    compare_s = 'hackerrank'
    count = 0
    if len(compare_s) > len(s):
        return 'NO'
    for i in compare_s:
        while count < len(s) and s[count] != i:
            count+=1
        if count == len(s):
            return 'NO'
        count +=1
    return 'YES'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
