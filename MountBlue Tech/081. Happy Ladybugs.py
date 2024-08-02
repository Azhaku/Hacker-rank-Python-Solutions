#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#
# if i != i-1 or i != i+1 and '_' not in b
# 
#
#
#


def happyLadybugs(b):
    
    counter = dict(Counter(b))
    spaces = False
    if '_' in counter:
        counter.pop("_")
        spaces = True
    print(counter)
    if 1 in counter.values():
        return 'NO'
    elif not spaces and any(b[x-1] != b[x] and b[x] != b[x+1] for x in range(1, len(b)-1)):
        return 'NO'
    else:
        return 'YES'
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()

    
    
    
    