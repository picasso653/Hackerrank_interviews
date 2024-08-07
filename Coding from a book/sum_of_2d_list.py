def sum_2d_list(arr):
    sum = 0
    for _ in arr:
        for i in _:
            sum+= i
    return sum