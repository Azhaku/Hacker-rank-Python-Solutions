#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    n = len(grid)
    res = []
    for i in range(0, n):
        s = ""
        for j in range(0,  n):
            if i == 0 or i == n-1 or j ==0 or j == n-1:
                s += grid[i][j]
            else:
                adj = 0
                if grid[i][j] > grid[i][j-1]:
                    adj +=1
                if grid[i][j] > grid[i][j+1]:
                    adj +=1
                if grid[i][j] > grid[i-1][j]:
                    adj +=1
                if grid[i][j] > grid[i+1][j]:
                    adj +=1
                if adj == 4:
                    s+= 'X'
                else:
                    s+= grid[i][j]
        res.append(s)
    return res
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
