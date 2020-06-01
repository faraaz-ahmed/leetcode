class Solution:
  def arrayRankTransform(self, arr: List[int]) -> List[int]:
    rank = list(set(arr))
    rank.sort()
    h = {}
    for i in range(0, len(rank)):
      h[rank[i]] = i + 1
    # keys = h.keys()
    ans = []
    for i in range(0, len(arr)):
      ans.append(h[arr[i]])
    return ans
