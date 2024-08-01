"""Given a list of positive and negative integer s, find a contiguous subarray whose
sum (sum of elements) is maximized.
"""
def maxSubArraySum(lst):
    size = len(lst)
    maxSoFar = 0
    maxEndingHere = 0
    i = 0
    while i < size:
        maxEndingHere = maxEndingHere + lst[i]
        if maxEndingHere < 0:
            maxEndingHere = 0
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere
        i += 1
    return maxSoFar
    
print(maxSubArraySum([1, -2, 3, 4, -4, 6, -4, 8, 2]))