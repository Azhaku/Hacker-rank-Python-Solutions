#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # a = set(arr)
    # print(a)
    # b = set(brr)
    # print(b-a)
        # res = set()
        # dic= {}
        # for i in arr:
        #     if i in dic:
        #         dic[i] +=1
        #     else:
        #         dic[i] = 1
        # for i in brr:
        #     if i in dic:
        #         if dic[i]==0:
        #             res.add(i)
        #         else:
        #             dic[i] -=1
        #     else:
        #         res.add(i)
        # return res
    res = set()
    if len(arr) == 0:
        return sorted(brr)
    arr.sort()
    brr.sort()
    l = r = 0
    while l<len(arr) and r<len(brr):
        if arr[l] == brr[r]:
            # print(arr[l],brr[r])
            l+=1
            r+=1
        else:
            # print('else')
            while r<len(brr) and arr[l] != brr[r]:
                res.add(brr[r])
                # print('hi')
                r += 1
                
    while r<len(brr):
        res.add(brr[r])
        r+=1
    res = sorted(list(res))
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
