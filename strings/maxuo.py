letters = [ 'a', 'b', 'ć', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'y', 'z'];
result = []

def gc(arr1, arr2):
  temp = arr1
  result = []
  for i in range(0, len(temp)):
    for j in range(0, len(arr2)):
      result.append(temp[i] + arr2[j])
  return arr1 + result

print(gc(gc(gc(gc, letters), letters), letters), letters)

