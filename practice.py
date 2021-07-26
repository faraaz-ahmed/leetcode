# a = list(map(int, input().split(' ')))
# print((a[0] + 2 * a[1]) / 3)

# dic = {'H': '0', '2B': '1', '3B': '2', 'HR': '3'}
# check = [1] * 4
# for i in range(0, 4):
#   s = input()
#   for key in dic.keys():
#     if (s == key):
#       check[int(dic[key])] -= 1
# flag = True
# for val in check:
#   if val > 0:
#     flag = False
#     break
# print('Yes' if flag else 'No')

from os import X_OK


s = input()
dic = {}
for char in 'chokudai':
  dic[char] = []
for i in range(0, len(s)):
  if s[i] in dic.keys():
    dic[s[i]].append(i)
sum = 0
for char in 'chokuda':
  if char == 'c':
    for i in range(0, len(dic['c'])):
      sum += len(filter(lambda x: x > dic['c'][i], dic['h']))
  if char == 'h':
    for i in range(0, len(dic['h'])):
      sum += len(filter(lambda x: x > dic['h'][i], dic['o']))
  if char == 'o':
    for i in range(0, len(dic['o'])):
      sum += len(filter(lambda x: x > dic['o'][i], dic['k']))
  if char == 'k':
    for i in range(0, len(dic['k'])):
      sum += len(filter(lambda x: x > dic['k'][i], dic['u']))
  if char == 'u':
    for i in range(0, len(dic['u'])):
      sum += len(filter(lambda x: x > dic['u'][i], dic['d']))
  if char == 'd':
    for i in range(0, len(dic['d'])):
      sum += len(filter(lambda x: x > dic['d'][i], dic['a']))
  if char == 'a':
    for i in range(0, len(dic['a'])):
      sum += len(filter(lambda x: x > dic['a'][i], dic['i']))
print(sum)




