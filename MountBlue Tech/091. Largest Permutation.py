#!/bin/python3

import math
import os
import random
import re
import sys


def largestPermutation(k, arr):
    a = dict(enumerate(arr)) 

    b = {v:k for k,v in a.items()} 
    l = len(arr)
    for i in range(l): 
        if k and a[i]!=l-i:
            x = a[i]
            y = b[l-i]

            a[i] = l-i
            a[y] = x
            b[x] = y
            k-=1 
        yield a[i] 
n,k = map(int,input().split())
arr = list(map(int,input().split()))
print(*largestPermutation(k, arr))