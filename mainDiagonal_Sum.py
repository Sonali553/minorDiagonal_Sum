lst = list(map(int, input().split()))
def mainDiagonal_Sum(lst):
  n = len(lst)
  i = 2
  res = 0
  while(i < n):
    res += lst[i]
    i += (lst[1] + 1)
  return res
  
print(mainDiagonal_Sum([3, 3, 1, -2, -3, -4, 5, -6, -7, -8, 9]))
print(mainDiagonal_Sum([2, 2, 3, 2, 2, 3]))
print(mainDiagonal_Sum([4, 4, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]))
print(mainDiagonal_Sum(lst))