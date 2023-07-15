array = list(map(int, input().split()))
def subArray_Sum(array):
    res = 0
    for i in range(0, len(array)):
        s = 0
        for j in range(i, len(array)):
            s += array[j]
            res += s
    return res
print(subArray_Sum([1, 2, 3]))
print(subArray_Sum([2, 1, 3]))
print(subArray_Sum(array))