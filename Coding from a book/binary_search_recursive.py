def binary_search(lst, value, high, low):
    mid = high+low//2
    if lst[mid] == value:
        return mid
    if lst[mid] > value:
        return binary_search(lst, value, mid-1, low)
    else:
        return binary_search(lst, value, high, mid+1)