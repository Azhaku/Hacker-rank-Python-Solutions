#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    status = 1
    move = 0
    while n>1:
        if n&(n-1) == 0:
            move+=1
            n = n>>1
        else:
            n = n - (1<<n.bit_length()-1)
            move +=1
    
    if move&1 == 1:
        return 'Louise'
    return 'Richard'
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
