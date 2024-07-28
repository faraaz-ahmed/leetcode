class Solution:
    def isBad(self, a, b):
        return ((a.lower() == b and a.isupper()) or (a == b.lower() and b.isupper()))

    def makeGood(self, s: str) -> str:
        l = -1
        while not len(s) == l:
            i = 0
            l = len(s)
            while i + 1 < len(s):
                if self.isBad(s[i], s[i + 1]):
                    # print(s, '1')
                    s = s[:i] + s[i + 1:]
                    # print(s, '2')
                    s = s[:i] + s[i + 1:]
                    # print(s, '3')
                else:
                    i += 1
            # print(len(s), l)
        return s
