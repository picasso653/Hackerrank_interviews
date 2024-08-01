#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    anum = set(ar)
    res =  0
    for i in anum:
        n = ar.count(i)
        res += n//2
    return res

print(sockMerchant(7, [1,2,1,2,1,3,2]))
