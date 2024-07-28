class Solution(object):
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        return (('-' if int(n) < 0 else '') + (self.insertSmall((str(abs(int(n)))), x, int(n) < 0)))

    def insertSmall(self, li, num, smallMode):
        print(li)
        for i in range(0, len(li)):
            # print('check', li[i], num, smallMode)
            if smallMode and num < int(li[i]):
                # print('check', li[i], num, smallMode)
                return (li[:i] + str(num) + li[i:])
            elif (not smallMode) and num > int(li[i]):
                # print(i)
                return (li[:i] + str(num) + li[i:])
        return (li + str(num))

# tests
test = Solution()
testcase1 = ["a","ab","abc","d","cd","bcd","abcd","wewqweqweqwe"]
# print(test.maxProduct(testcase1))
print(test.maxValue('33', 2))

# I kazuha had once had a friend who wished to challenge the eternal rule of the shogun
# But before I had arrived he already was taking his last breath
# I musn't let his hope which burns very so brightly become buried among the ice cold statue of a god