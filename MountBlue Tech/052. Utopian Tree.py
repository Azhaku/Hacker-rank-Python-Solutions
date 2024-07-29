#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # count = 0
    # hei = 1
    # while n > count:
    #     hei += hei
    #     count += 1
    #     if n > count:
    #         hei += 1
    #         count +=1
    # return hei
    
    if n % 2 == 0:
        return (2 ** ((n // 2) + 1)) - 1
    else:
        return (2 ** (((n + 1) // 2) + 1)) - 2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

