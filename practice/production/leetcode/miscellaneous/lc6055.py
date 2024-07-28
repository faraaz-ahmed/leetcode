class Solution:
  def convertTime(self, current: str, correct: str) -> int:
    currentTime = int(current[:2]) * 60 + int(current[3:])
    correctTime = int(correct[:2]) * 60 + int(correct[3:])
    # print(currentTime, correctTime)
    # print(current[:2])
    diff = correctTime - currentTime
    count = 0
    count += diff // 60
    # print(count, diff)
    diff = diff % 60
    # print(diff)
    count += diff // 15
    diff = diff % 15
    count += diff // 5
    diff = diff % 5
    count += diff
    return count