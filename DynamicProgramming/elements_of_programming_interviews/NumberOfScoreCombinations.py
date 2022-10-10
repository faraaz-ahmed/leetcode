def solution(final_score, scores):
  num_combinations_for_score = [[1] + [0] * final_score for _ in scores]
  for i in range(0, len(scores)):
    for j in range(1, final_score + 1):
      without_this_play = (num_combinations_for_score[i - 1][j] if i >= 1 else 0)
      with_this_play = num_combinations_for_score[i][j - scores[i]] if j >= scores[i] else 0 + num_combinations_for_score[i - 1][j] if i >= 0 else 0
      num_combinations_for_score[i][j] = without_this_play + with_this_play
