#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    time_db = {
        1: 'one', 2: 'two', 3: 'three', 4: "four", 5: "five",6: "six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
        11: "eleven", 12: "twelve",13: "thirteen", 14:"fourteen",16: "sixteen", 17:"seventeen", 18:"eighteen",
        19: "nineteen", 20: "twenty", 21:"twenty one",22:"twenty two",23: "twenty three", 24:"twenty four",
        25:"twenty five", 26:"twenty six", 27: "twenty seven",28: "twenty eight", 29: "twenty nine"}
    if not m:
        return f"{time_db[h]} o' clock"
    elif m == 1:
        return f"one minute past {time_db[h]}"
    elif m == 59:
        return f"one minute to {time_db[h+1]}"
    elif m == 15:
        return f"quarter past {time_db[h]}"
    elif m == 30:
        return f"half past {time_db[h]}"
    elif m == 45:
        return f"quarter to {time_db[h+1]}"
    elif m<=29:
        return f"{time_db[m]} minutes past {time_db[h]}"
    else:
        return f"{time_db[60 - m]} minutes to {time_db[h+1]}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
