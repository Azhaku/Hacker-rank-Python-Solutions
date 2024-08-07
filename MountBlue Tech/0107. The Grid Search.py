#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#
def check(G,P,i,j,trow,tcol):
    for ii in range(trow):
        for ij in range(tcol):
            if G[i+ii][j+ij] != P[ii][ij]:
                return False
    return True

def gridSearch(G, P):
    row = len(G)
    col = len(G[0])
    trow = len(P)
    tcol = len(P[0])
    for i in range(row - (trow-1)):
        for j in range(col - (tcol -1)):
            if G[i][j] == P[0][0]:
                if check(G,P,i,j,trow,tcol):
                    return "YES"
                        
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
