# problem
# https://www.hackerrank.com/challenges/arrays-ds/problem

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):    
    # Write your code here
    ptr_2 = len(a)-1
    ptr_1 = 0
    while ptr_1 < ptr_2:
        temp = a[ptr_1]
        a[ptr_1] = a[ptr_2]
        a[ptr_2] = temp
        ptr_1 = ptr_1+1
        ptr_2 = ptr_2-1
    return a
    
           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

