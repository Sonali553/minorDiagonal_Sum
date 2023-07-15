Arr_len, Limit_val = map(int, input().split())
L = list(map(int, input().split()))
def max_subarray_sum(Arr_len, Limit_val, L):
    res = 0
    for i in range(0, len(L)):
        subarray_sum  = 0
        for j in range(i, len(L)):
            subarray_sum += L[j]
            if subarray_sum <= Limit_val and Limit_val > res:
                res = subarray_sum
    return res
print(max_subarray_sum(5, 12, [2, 1, 3, 4, 5]))
print(max_subarray_sum(3, 1, [2, 2, 2]))
print(max_subarray_sum(Arr_len, Limit_val, L))