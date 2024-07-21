#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    rem_energy = 100
    
    jump = (0+k)%len(c)
    rem_energy = 3 if c[jump]!=0 else 1
        
    while jump != 0:
        jump = (jump+k)%len(c)
        rem_energy = 3 if c[jump]!=0 else 1
    return rem_energy
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
