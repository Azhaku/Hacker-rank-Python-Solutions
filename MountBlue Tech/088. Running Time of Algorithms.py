#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(l):
    res = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j > -1) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
           res += 1
        l[j+1] = key
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
