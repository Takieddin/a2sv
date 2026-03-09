#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    i = n - 2
    end = False
    tmp = arr[n - 1]
    while i >= 0:
        if arr[i] >= tmp:
            arr[i + 1] = arr[i]
            i -= 1
        else:
            arr[i + 1] = tmp
            end = True
        res = " ".join(list(map(str,arr)))
        print(res)
        if end:
            break
    if not end:
        arr[0] = tmp
        res = " ".join(list(map(str,arr)))
        print(res)
        
    
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
