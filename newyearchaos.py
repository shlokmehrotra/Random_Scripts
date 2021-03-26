# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
#need to fix runtime

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    def solution():
        init = [i for i in range(1, len(q) + 1)]
        #init = list(range(1, len(q)+1))
        switch_counts = [0] * len(q)
        def overcount():
            for i in range(len(switch_counts)):
                if switch_counts[i] > 2:
                    return -1
            return 0
        def swap(index):#index that is being swapped w/ element in front
            temp = init[index-1]
            init[index-1] = init[index]
            init[index] = temp
        for i in range(len(init)):
            while(init[i] != q[i]):
                #index of element that is being looked for: init.find(q[i])
                swap(init.index(q[i]))
                switch_counts[q[i]-1] += 1
                if(overcount() == -1):
                    return "Too chaotic"
        #print(init)
        return(sum(switch_counts))
    print(solution())
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
