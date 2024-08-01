def rotateArray(lst, k):
    return lst[k:] + lst[0:k]

print(rotateArray([10,20,30,40,50,60,70], 2))