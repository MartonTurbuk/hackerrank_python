#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the findDigits function below.

def findDigits(n):
    count = 0
    for num in list(str(n)):
        if int(num) != 0 and int(n) % int(num) == 0:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
