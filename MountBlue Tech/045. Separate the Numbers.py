#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def generateNums(s,itr):
    if len(s)==1:
        return 0
    prev = int(s[:itr])
    ns = s[:itr]
    while True:
        if len(ns) >= len(s):
            break
        ns += str(prev+1)
        prev = prev+1
    if ns == s:
        return 1
    return 0
        
def separateNumbers(s):
    l = (len(s)//2)+1 if len(s)>2 else len(s)//2
    for i in range(l):
        res = generateNums(s,i+1)
        if res:
            print(f'YES {s[:i+1]}')
            return None
    print('NO')
    

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
