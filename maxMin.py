#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxMin' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY operations
#  2. INTEGER_ARRAY x
#

def maxMin(operations, x):
    # Write your code here
    elements = []
    minimum = 0
    maximum = 0
    products = []
    for i,j in zip(operations, x):
        if i == "push":
            elements.append(j)
        else:
            elements.remove(j)

    return None

print(maxMin(["push", 'push', 'push', 'pop'], [1,2,3,1]))