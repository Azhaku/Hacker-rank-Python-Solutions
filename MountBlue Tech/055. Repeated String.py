#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter as freq



# sample i/p and o/p
# a
# 1000000000000

# 1000000000000


# aba
# 10

# 7


def repeatedString(s, n):
    ls = len(s)
    count = freq(s)
    quo = n//ls
    rem = n%ls
    res = quo*count['a']
    res += freq(s[:rem])['a']
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
