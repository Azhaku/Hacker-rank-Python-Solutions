#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    sorted_a = sorted(a)
    dic = {}
    for i in sorted_a:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    res = 0
    for key in dic:
        if key+1 in dic:
            res = max(res,dic[key]+dic[key+1])
        else:
            res = max(res, dic[key])
    return res
                   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
