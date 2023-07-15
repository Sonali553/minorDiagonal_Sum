Arr_len, Limit_val = map(int, input().split())
L = list(map(int, input().split()))
def max_subarray_sum2(Arr_len, Limit_val, L):
    current_sum = 0
    j = 0
    res = 0
    for i in range(0, Arr_len):
        current_sum += L[i]
        while(current_sum > Limit_val):
                 current_sum -= L[j]
                 j += 1
        res = max(res, current_sum)
    return res

print(max_subarray_sum2(5, 12, [2, 1, 3, 4, 5]))
print(max_subarray_sum2(3, 1, [2, 2, 2]))
print(max_subarray_sum2(Arr_len, Limit_val, L))
