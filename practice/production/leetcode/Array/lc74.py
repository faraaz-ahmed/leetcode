class Solution:
  def binarySearch(self, arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
      mid = (low + high) // 2
      if target < arr[mid]:
        high = mid - 1
      elif target > arr[mid]:
        low = mid + 1
      else:
        return True
    return False
            
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    n, selectedRow = len(matrix), -1
    for j in range(0, n):
      if target >= matrix[j][0]:
        selectedRow += 1
      else:
        break
    if selectedRow == -1:
      selectedRow = 0
    return self.binarySearch(matrix[selectedRow], target)
        
        

# print(binarySearch([1,2,3,4,5], 3))
# for i in range(0, 7):
#   print(i)
#   print(binarySearch([1,2,3,4,5], i))