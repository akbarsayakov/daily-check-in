
def backtrack(res, num, n):
  if num == n:
    return res

  if (num >= 0):
    res = res + num
    return backtrack(res, num + 1, n)

print(backtrack(0, 0, 10))