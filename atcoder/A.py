def copy(arr):
  res = []
  for item in arr:
    res.append(item)
  return res
a = [1,2,3]
c = a
c.append('ok')
b = copy(a)
b[1] = 4
b.append(5)
print(a, b)