n = int(input())
def arranging_coins(n):
  if n == 0:
    return 0
  if n == 1:
       return 1 
  for stair in range(1, n):
     n = n - stair
     if n < 0:
       return stair - 1
     
print(arranging_coins(5))
print(arranging_coins(8))
print(arranging_coins(n))