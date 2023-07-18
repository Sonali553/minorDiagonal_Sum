n = int(input())
lst = []
for i in range(0, n):
    l = list(map(int, input().split()))
    lst.append(l)
def minorDiagonal_Sum(lst):
    N = len(lst)
    res = 0
    for i in range(0, len(lst)):
        res += lst[i][N - 1 -i]
    return res

print(minorDiagonal_Sum([[1, -2, -3], [-4, 5, -6], [-7, -8, 9]]))
print(minorDiagonal_Sum([[3, 2], [2, 3]]))
print(minorDiagonal_Sum(lst))