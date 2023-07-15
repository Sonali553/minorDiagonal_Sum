Array = list(map(int, input().split()))
L, R = map(int, input().split())
def subarrayInRange(Array, L, R):
    result = [Array[i] for i in range(L, R + 1)]
    return result
print(subarrayInRange([4, 3, 2, 6], 1, 3))
print(subarrayInRange([4, 2, 2], 0, 1))
print(subarrayInRange(Array, L, R))
    