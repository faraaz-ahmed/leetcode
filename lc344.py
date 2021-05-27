class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(0, int(length / 2)):
            s[i], s[length - 1 - i] = s[length - 1 -i], s[i]
        return s
