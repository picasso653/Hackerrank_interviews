#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    num = len(arr)
    num_neg = 0
    num_pos = 0
    num_zero = 0

    for i in arr:
        if i < 0:
            num_neg += 1
        elif i > 0:
            num_pos += 1
        else:
            num_zero += 1

    return "{:.6f}".format((num_neg/num)), "{:.6f}".format((num_pos/num)), "{:.6f}".format((num_zero/num))

print(plusMinus([1, 1, -1, -2, 0]))