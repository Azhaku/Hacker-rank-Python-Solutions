#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    arr.sort()
    dic = defaultdict(list)
    for i in range(1, len(arr)):
        diff = abs(arr[i-1] - arr[i])
        if diff in dic:
            dic[diff].append(arr[i-1])
            dic[diff].append(arr[i])
        else:
            dic[diff] = [arr[i-1],arr[i]]
    return(dic[min(dic.keys())])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
