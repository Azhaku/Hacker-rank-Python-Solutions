#!/bin/python3

import math
import os
import random
import re
import sys

def calSum(n):
    total = 0
    for i in str(n):
        total += int(i)
    return total

def superDigit(n, k):
    res = 0
    n = calSum(n)*k
    while n >= 10:
        n = calSum(n)
    return n
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
