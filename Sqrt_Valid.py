n = int(input())
def sqrt_valid(n):
  for ele in range(0, n+1):
    if ele * ele == n:
        return True
  return False
print(sqrt_valid(n))
print(sqrt_valid(14))
print(sqrt_valid(16))



