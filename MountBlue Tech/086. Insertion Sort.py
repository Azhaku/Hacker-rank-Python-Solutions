#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    element = arr[-1]
    i = len(arr) - 2
    while i > -1 and element < arr[i]:
        arr[i+1] = arr[i] 
        i -=1
        print(" ".join(map(str, arr)))
    arr[i+1] = element
    print(" ".join(map(str, arr)))
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
