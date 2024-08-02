#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    a = sorted(arr)
    res = []
    while a:
        res.append(len(a))
        count = len(a)
        sub = a[0]
        for i in range(count):
            a[i] -=sub
        status = 1
        while status:
            if a and a[0] == 0:
                a.pop(0)
            else:
                status = 0
    return res
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
