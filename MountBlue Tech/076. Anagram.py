#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    size = len(s)
    if size & 1 == 1:
        return -1
    half = size//2
    
    #create a freq dic
    dic = {}
    for i in range(half, size):
        if s[i] in dic:
            dic[s[i]] += 1
        else:
            dic[s[i]] =1
    res = 0
    print(dic)
    for i in range(half):
        if s[i] in dic:
            if dic[s[i]] == 0:
                res += 1
            else:
                dic[s[i]] -=1
        else:
            res += 1
        
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
