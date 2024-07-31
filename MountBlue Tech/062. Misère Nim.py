#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def misereNim(s):
    #  if there is only 1 pile AND it has more than 1 element => First player wins
    if n == 1:
        return "First" if s[0] > 1 else "Second"
    total = s[0]
    xor = s[0]

    for i in range(1,n):
        total += s[i]
        xor ^= s[i]
    """
        If sum of all stones equals the total piles, all piles have a single (1)
        stone. For even number of piles, first player will always win.
        """
    if total == n:
        return "First" if total & 1 == 0 else "Second"
    """
        For all other cases, the xor value determines winner. If xor value = 0, then
        second player will always win as all piles (stones) can be paired.
        """
    return  "First" if xor > 0 else "Second"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
