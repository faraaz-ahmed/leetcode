class Solution:
  def binarySearch(self, arr, val):
    low, high = 0, len(arr) - 1
    while low <= high:
      mid = (low + high) // 2
      print(mid, low, high, val, arr[mid])
      
      if val > arr[mid]:
        low = mid + 1
      elif val < arr[mid]:
        high = mid
      else:
        return mid
      if low == high:
        if val == arr[mid]:
          return mid
        else:
          return False
    return False
  
  def canReorderDoubled(self, arr: List[int]) -> bool:
    arr2 = list(filter(lambda x: not x == 0, arr))
    if not (len(arr) - len(arr2)) % 2 == 0:
      return False
    arr2.sort()
    i = 0
    while i < len(arr2):
      find = self.binarySearch(arr2, arr2[i] * 2) if arr2[i] > 0 else self.binarySearch(arr2, arr2[i] // 2)
      print('kek', find)
      if not find == False:
        del arr2[find]
        del arr2[i]
        print('arr', arr2)
      else:
        return False
    return True
        
        