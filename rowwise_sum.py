r, c = map(int, input().split())
lst = []
for i in range(0, r):
    l = list(map(int, input().split()))
    lst.append(l)
def rowSum2D(lst):
    res = []
    for i in range(0, len(lst)):
        r = 0
        for j in range(0, len(lst[0])):
              r += lst[i][j]
        res.append(r)
    return res
print(rowSum2D([ [1,2,3,4], [5,6,7,8], [9,2,3,4] ]))
print(rowSum2D(lst))