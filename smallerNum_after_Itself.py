lst = list(map(int, input().split()))
def count_SmallNum_toRight(lst):
  res = []
  for i in range(0, len(lst)):
    r = 0
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            r += 1
    res.append(r)
  return res
print(count_SmallNum_toRight([5, 2, 6, 1]))
print(count_SmallNum_toRight([-1]))
print(count_SmallNum_toRight([-1, -1]))
print(count_SmallNum_toRight(lst))