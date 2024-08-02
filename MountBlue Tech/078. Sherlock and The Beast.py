#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(N): #eg:8
    if N < 3:
        print(-1)
    else:
        k = N - (N % 3)  #6

        if k < N: 
            while k > 0 and (N - k) % 5 > 0:
                k -= 3

        if (N - k) % 5 == 0:
            print(('5' * k) + ('3' * (N - k)))
        else:
            print(-1)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
