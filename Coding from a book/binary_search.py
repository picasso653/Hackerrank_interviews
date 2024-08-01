def binarySearch(lst, value, isSorted = True):
    size = len(lst)
    high = size -1
    low = 0
    while high >= low:
        mid = (high + low)//2
        if lst[mid] == value:
            return True
        elif lst[mid] > value:
            high = mid -1
        else: low = mid + 1
    return False


print(binarySearch([1,2,3,4,5,10,15,28,30,40,50,52,59,71,89], 8))