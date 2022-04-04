class Solution:
  def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    won, lost = {}, {}
    wonSet, lostSet = [], []
    for i in range(0, len(matches)):
      if not matches[i][0] in won:
        won[matches[i][0]] = 1
      else:
        won[matches[i][0]] += 1
      if not matches[i][1] in lost:
        lost[matches[i][1]] = 1
      else:
        lost[matches[i][1]] += 1
      # lost[matches[i][1]] = matches[i][1]
    # print(won, lost)
    result1, result2 = [], []
    result1 = list(set(won.keys()) - set(lost.keys()))
    result1.sort()
    for key in lost.keys():
      if lost[key] == 1:
        result2.append(key)
    result2.sort()
    return [result1, result2]
