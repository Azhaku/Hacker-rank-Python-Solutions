#!/bin/python3

import math
import os
import random
import re
import sys

# Code to be written by User.
def sumXor(n):
    return 2**(bin(n).count('0')-1)-bool(not n)


#Code snippet given by Hackkerrank.
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()