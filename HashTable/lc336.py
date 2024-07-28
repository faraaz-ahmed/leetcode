class Solution:
    def isPalin(self, word, i, j):  # taking indexes to prevent string generation
        while i < j:
            if not word[i] == word[j]:
                return False
            i += 1
            j -= 1
        return True

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        wordMap, answer = {}, []
        for i in range(len(words)):
            wordMap[words[i]] = i
        for i in range(len(words)):
            if words[i] == '':
                for j in range(len(words)):
                    if (not j == i) and self.isPalin(words[j], 0, len(words[j]) - 1):
                        answer.append([i, j])
                        answer.append([j, i])
            else:
                backwards = words[i][:: -1]
                if backwards in wordMap and (not i == wordMap[backwards]):
                    answer.append([i, wordMap[backwards]])
                for j in range(1, len(backwards)):
                    if self.isPalin(backwards, 0, j - 1) and backwards[j:] in wordMap:
                        answer.append([i, wordMap[backwards[j:]]])
                    if self.isPalin(backwards, j, len(backwards) - 1) and backwards[:j] in wordMap:
                        answer.append([wordMap[backwards[:j]], i])
        return answer