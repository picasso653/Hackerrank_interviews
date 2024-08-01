def maxSubsetSum(arr):
    final = []
    max_subarray_sum = 0
    max_subarray = []

    def get_non_adjacent_subsets(arr, idx=0, current=[]):
        if idx >= len(arr):
            return current.copy()
       
        subsets_with_current = get_non_adjacent_subsets(arr, idx + 2, current + [arr[idx]])
        final.append(subsets_with_current)
       
        subsets_without_current = get_non_adjacent_subsets(arr, idx + 1, current)
        final.append(subsets_without_current)
       
    #    return subsets_with_current + subsets_without_current
    
    get_non_adjacent_subsets(arr)

    for i in final:
        if i is None:
            continue
        if sum(i) > max_subarray_sum:
            max_subarray = i.copy()
            max_subarray_sum = sum(i)

    return max_subarray_sum