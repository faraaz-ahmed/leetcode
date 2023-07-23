# 1680. Concatenation of Consecutive Binary Numbers
# Medium

# 571

# 277

# Add to List

# Share
# Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

 

# Example 1:

# Input: n = 1
# Output: 1
# Explanation: "1" in binary corresponds to the decimal value 1. 
# Example 2:

# Input: n = 3
# Output: 27
# Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
# After concatenating them, we have "11011", which corresponds to the decimal value 27.
# Example 3:

# Input: n = 12
# Output: 505379714
# Explanation: The concatenation results in "1101110010111011110001001101010111100".
# The decimal value of that is 118505380540.
# After modulo 109 + 7, the result is 505379714.
 

# Constraints:

# 1 <= n <= 105
# Accepted
# 45,507
# Submissions
# 83,592






class Solution:
  def concatenatedBinary(self, n: int) -> int:
    nums = ['0', '1']
    result = '1'
    if n <= 1:
      return nums[1]
    
    def getNextBinary(num):
      i = len(num) - 1
      index = 'None'
      print('i', i, num, num[i])
      while i >= 0:
        print('check1', num[i])
        if num[i] == '0':
          print('check 2', num[i])
          index = i
          print('i and index', i, index)
          break
        i -= 1
      print('index', index, num)
      if index == 'None':
        return '1' + '0' * len(num)
      else:
        return num[:index] + '1' + '0' * (len(num) - (index + 1))

    i = 2
    while i <= n:
      nums.append(getNextBinary(nums[i - 1]))
      print('ok', nums)
      result += nums[len(nums) - 1]
      print('result', result)
      i += 1
      
    return int(result, 2) % (10 ** 9 + 7)

class AcceptedSolution:
    def concatenatedBinary(self, n: int) -> int:
        string = ""
        for i in range(1,n+1):
            string+=format(i,"b")
        return int(string,2)%(10**9 + 7)
        