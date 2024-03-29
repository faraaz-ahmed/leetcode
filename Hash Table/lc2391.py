# 2391. Minimum Amount of Time to Collect Garbage
# Medium
# 1.4K
# 201
# Companies
# You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.

# You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.

# There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.

# Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.

# Return the minimum number of minutes needed to pick up all the garbage.

 

# Example 1:

# Input: garbage = ["G","P","GP","GG"], travel = [2,4,3]
# Output: 21
# Explanation:
# The paper garbage truck:
# 1. Travels from house 0 to house 1
# 2. Collects the paper garbage at house 1
# 3. Travels from house 1 to house 2
# 4. Collects the paper garbage at house 2
# Altogether, it takes 8 minutes to pick up all the paper garbage.
# The glass garbage truck:
# 1. Collects the glass garbage at house 0
# 2. Travels from house 0 to house 1
# 3. Travels from house 1 to house 2
# 4. Collects the glass garbage at house 2
# 5. Travels from house 2 to house 3
# 6. Collects the glass garbage at house 3
# Altogether, it takes 13 minutes to pick up all the glass garbage.
# Since there is no metal garbage, we do not need to consider the metal garbage truck.
# Therefore, it takes a total of 8 + 13 = 21 minutes to collect all the garbage.
# Example 2:

# Input: garbage = ["MMM","PGM","GP"], travel = [3,10]
# Output: 37
# Explanation:
# The metal garbage truck takes 7 minutes to pick up all the metal garbage.
# The paper garbage truck takes 15 minutes to pick up all the paper garbage.
# The glass garbage truck takes 15 minutes to pick up all the glass garbage.
# It takes a total of 7 + 15 + 15 = 37 minutes to collect all the garbage.
 

# Constraints:

# 2 <= garbage.length <= 105
# garbage[i] consists of only the letters 'M', 'P', and 'G'.
# 1 <= garbage[i].length <= 10
# travel.length == garbage.length - 1
# 1 <= travel[i] <= 100

class Solution:
  # algo:
    # for each type of truck:
    #   frequency(type) eg: frequency(glass) = 4, frequency(paper) = 2, frequency(metal) = 0,
    #   last_index_occurence(type)  last_index_occurence(glass) = 3
    #   last_index_occurence(paper) = 2
      
    # paper => (2 + 4) + 2 = 8 mins
    # [2, 6, 9]
    # glass => (2 + 4 + 3) + 4 = 13 mins
    # total => 21 mins
  def computeFrequency(garbage: List[str]):
    frequency_ = {'G': 0, 'P': 0, 'M': 0}
    for str_ in garbage:
      for char_ in str_:
        if char_ in frequency_:
          frequency_[char_] += 1
        else:
          frequency_[char_] = 0
    return frequency_

  def computeLastIndexOccurence(garbage: List[str]):
    last_index_occurence = {'G': 0, 'P': 0, 'M': 0}
    for i in range(0, len(garbage)):
      for char_ in garbage[i]:
        if char_ in last_index_occurence:
          last_index_occurence[char_] = i
        else:
          last_index_occurence[char_] = 0
    return last_index_occurence

  def computeTimeForEachTruck(type_, frequency_, last_index_occurence, continuous_sum):
    if type_ in frequency_:
      if frequency_[type_] > 0:
        if last_index_occurence[type_] == 0:
          return frequency_[type_]
        return continuous_sum[last_index_occurence[type_] - 1] + frequency_[type_]
    return 0


  def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
    types_ = ['G', 'P', 'M']
    frequency_ = Solution.computeFrequency(garbage)
    last_index_occurence = Solution.computeLastIndexOccurence(garbage)
    continuous_sum = []
    current_sum = 0
    for time in travel:
      current_sum += time
      continuous_sum.append(current_sum)
    
    result = 0
    for type_ in types_:
      result += Solution.computeTimeForEachTruck(type_, frequency_, last_index_occurence, continuous_sum)
    return result
    


    



