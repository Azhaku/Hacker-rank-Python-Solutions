#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s hackerhappy
#  2. STRING t hackerrank
#  3. INTEGER k 9
#

def appendAndDelete(s, t, k):
    count =0
    while len(s) > count < len(t) and s[count] == t[count]:
        count +=1
    # sl = len(s) - count
    # tl = len(t) - count
    # if sl + tl <= k :
    #     return 'Yes'
    # return 'No'
    t_len = len(s) + len(t)
    if t_len <= 2*count+k and t_len%2 == k%2 or t_len < k:
        return 'Yes'
    return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
