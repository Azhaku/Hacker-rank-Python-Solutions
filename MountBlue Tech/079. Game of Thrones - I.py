#!/bin/python3

import math
import os
import random
import re
import sys


def gameOfThrones(s):
    dic = {}
    for i in s:
        if i in dic:
            del dic[i]
        else:
            dic[i] = 1
    return 'YES' if len(dic) <= 1 else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
