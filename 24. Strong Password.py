#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    spc = "!@#$%^&*()-+"
    li = [0]*4
    for i in password:
        if i.isdigit():
            li[0] = 1
        elif i.isupper():
            li[1] =1
        elif i in spc:
            li[2] = 1
        elif i.islower():
            li[3] = 1
    return max(6 - len(password) ,4 - sum(li))
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    password = input()
    answer = minimumNumber(n, password)
    fptr.write(str(answer) + '\n')
    fptr.close()
