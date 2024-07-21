#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
# def getMoneySpent(keyboards, drives, b):
#     if not (min(keyboards) + min(drives) < b):
#         return -1
#     res = 0
#     for kb in keyboards:
#         if kb < b:
#             for d in drives:
#                 tot = kb+d
#                 res = max(res ,tot if kb+d <=b else res)
#     return res

def getMoneySpent(kb, d, b):
    kb.sort()
    d.sort()
    i,j = 0, len(d)-1
    res = -1
    while i < len(kb) and j >=0 :
        tot = kb[i] + d[j]
        if tot > b:
            j -=1
        else:
            res = max(res,tot)
            i +=1
    return res
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
