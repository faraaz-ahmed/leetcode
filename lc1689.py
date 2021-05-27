class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        count = 0
        while n > 0:
            reducedVal = self.getReducedValue(n)
            n = reducedVal[0]
            count += reducedVal[1]
        return count

    def getReducedValue(self, number):
        strVal = str(number)
        reduced = "0"
        for i in range(1, len(strVal)):
            reduced += '0' if strVal[0] >= strVal[i] else str(int(strVal[i]) - int(strVal[0]))
        reduced = int(reduced)
        if reduced > 0:
            return [reduced, int(strVal[0])]
        else:
            return [0, int(strVal[0])]





# def isDeciBinary(number):
