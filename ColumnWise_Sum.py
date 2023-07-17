r, c = map(int, input().split())
lst = []
for i in range(0, r):
    l = list(map(int, input().split()))
    lst.append(l)
def columnSum(lst):
    res = []
    for i in range(0, len(lst[0])):
        r = 0
        for j in range(0, len(lst)):
              r += lst[j][i]
        res.append(r)
    return res

print(columnSum(
 [ [1,2,3,4],
   [5,6,7,8],
   [9,2,3,4] ]))
print(columnSum(lst))

