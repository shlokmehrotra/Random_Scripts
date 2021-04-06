#!/bin/python3
#https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    desired = sorted(arr)
    swaps = 0
    def find_index():
        for i in range(len(desired)):
            if(desired[i] != arr[i]):
                return i
        return -1
    while(desired != arr):
        fix_index = find_index()
        #swap arr[fix_index] and arr[arr.index(desired[fix_index])]
        temp = arr[arr.index(desired[fix_index])]
        arr[arr.index(desired[fix_index])] = arr[fix_index] 
        arr[fix_index] = temp
        swaps += 1
    return swaps
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
