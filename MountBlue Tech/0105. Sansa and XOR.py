#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# if size is even,  
# eg: [1,2] possible subsets = [[],[1],[2],[1,2]] all numbers will accure evenly so result will be zero
# if size is odd, 
# eg: [1] possible subsets = [[],[1]]
# eg: [1,2,3] possible subsets = [[],[1],[2],[3],[1,2],[2,3],[1,2,3]] subset [1,3] not included due to the questions nature
# freq = 1: 3, 2:4, 3:3



def sansaXor(arr):
    if len(arr)&1 == 0:
        return 0
    res = 0
    for i in range(0, len(arr),2):
        res ^= arr[i]
    return res
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
