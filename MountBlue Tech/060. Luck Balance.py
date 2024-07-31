#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    dic = {}
    # create a list of match importance(1 or 0)
    for lc,imp in contests:
        if imp not in dic:
            dic[imp] = [lc]
        else:
            dic[imp].append(lc)
    res = 0
    
    # save lucks in unimportant matches
    if 0 in dic:
        res += sum(dic[0])
    
    # sort the dic{ 1:[save top lucks], 1:[lose min lucks]}
    if 1 in dic:
        sorted_contests = sorted(dic[1], reverse = 1)
        print(sorted_contests)
        res += sum(sorted_contests[:k])
        res -= sum(sorted_contests[k:])
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
