#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    s, meridiem = s[:-2],s[-2:]
    si = [c for c in s.split(":")]
    if meridiem == 'PM' and int(si[0])<12:
        si[0] = str(12+int(si[0]))
    elif meridiem =="AM" and int(si[0]) == 12:
        si[0] = '00'
        
    return ":".join(si)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
