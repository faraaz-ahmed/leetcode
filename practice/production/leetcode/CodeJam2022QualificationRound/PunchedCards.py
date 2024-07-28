def getFirstRow(n):
  if n < 0:
    return
  elif n == 1:
    return '...'
  else:
    return '..' + '+-' * (n - 1) + '+'

def getSecondRow(n):
  if n < 0:
    return
  elif n == 1:
    return '...'
  else:
    return '..' + '|.' * (n - 1) + '|'

def getEvenRow(n):
  return '+-' * (n) + '+'

def getOddRow(n):
  return '|.' * (n) + '|'

def printResult(m, n):
  for i in range(0, (2 * m) + 1):
    if i == 0:
      print(getFirstRow(n))
    elif i == 1:
      print(getSecondRow(n))
    elif i % 2 == 0:
      print(getEvenRow(n))
    else:
      print(getOddRow(n))

t = int(input())
for i in range(0, t):
  [m, n] = list(map(int, input().split()))
  print("Case #" + str(i + 1) + ':')
  printResult(m, n)