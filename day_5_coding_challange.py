#!/bin/python3

import math
import os
import random
import re
import sys


def loop(num):
    if 2 <= num <= 20:
        for i in range(1, 11):
            print(f'{num} x {i} = {num * i}')


if __name__ == '__main__':
    n = int(input())
