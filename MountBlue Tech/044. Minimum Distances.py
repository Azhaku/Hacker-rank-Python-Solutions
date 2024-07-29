#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    n = len(a)
    mini = len(a)
    dic = {}
    for i in range(len(a)):
        if a[i] not in dic:
            dic[a[i]] = i
        else:
            mini = min(mini, i - dic[a[i]])
    return mini if mini< n else -1
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
