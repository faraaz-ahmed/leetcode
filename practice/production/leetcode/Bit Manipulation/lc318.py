# Straightforward solution is to compare each pair of words. We can use the fact that each word has only letters from a to z and for each word what is matter if it has some letter or not. Let d[word] be bitmask of word. For example for word aaabe we will have mask ...10011, here I for simplicity show only the last part, all other elements are zero. We have 1 in the end, because we have a in our word, we have 1 as next elements, because we have b, then we have 0, because we do not have c and so on. So, the whole algorithm can be separated into two stages:
#
# Compute all masks for all words, we will use d[word] |= 1<<(ord(l) - 97) for this, where 97 is code of symbol a. Also we use | (or) here to update zero-elements, but if we have one-elements, they will not change.
# For every pair of words check if d[w1] & d[w2] == 0, this is condition that pair of words will not have any intersections and update our ans if they not.
# Compexity
# Time complexity is O(n*s) + O(n^2), where s is the average length of word and n is number of words. Space complexity is O(n).

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bitmasks = []
        for i in range(0, len(words)):
            bitmasks.append(self.getBitmask(words[i]))
        max_ = 1
        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                # print("", int(bitmasks[i][26]) * int(bitmasks[j][26]), int(bitmasks[i][26]), int(bitmasks[j][26]), words[i], words[j])
                if int(bitmasks[i][0:26], 2) & int(bitmasks[j][0:26], 2) == 0 and max_ < int(bitmasks[i][26:]) * int(bitmasks[j][26:]):
                    # print("selected",int(bitmasks[i][26]) * int(bitmasks[j][26]), int(bitmasks[i][26]), int(bitmasks[j][26]), words[i], words[j])
                    max_ = int(bitmasks[i][26:]) * int(bitmasks[j][26:])
        return max_ if max_ > 1 else 0

    def getBitmask(self, word):
        bitmask = list("0" * 26)
        for i in range(0, len(word)):
            bitmask[ord(word[i]) - 97] = "1"
        bitmask = ''.join(bitmask)
        # print('word', word, len(word))
        bitmask += str(len(word))
        return bitmask

# tests
test = Solution()
testcase1 = ["a","ab","abc","d","cd","bcd","abcd","wewqweqweqwe"]
# print(test.maxProduct(testcase1))
print(test.getBitmask(testcase1[len(testcase1) - 1]))
