#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    level = 0
    valley = 0
    hill = 0
    is_below = path[0] == "U"
    for i in path:
        if i == "U":
            level += 1
        else:
            level -= 1
        if level > 0 and is_below == True:
            is_below = False
            hill += 1
        elif level < 0 and is_below == False:
            is_below = True
            valley += 1
        elif level == 0:
            is_below = False
        
    return valley


print(countingValleys(8, "UDDDUDUU"))