#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    count = [0,0,0]
    n = len(arr)
    for i in arr:
        if i > 0:
            count[0] +=1 
        elif i< 0:
            count[1] +=1
        else:
            count[2] +=1
    for i in count:
        print(round(i/n,6))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
