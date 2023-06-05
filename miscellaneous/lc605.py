'''
605. Can Place Flowers
Easy
4.7K
817
Companies
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
Accepted
413.5K
Submissions
1.3M
Acceptance Rate
32.9%
'''


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        if length == 1:
            n -= 1 if flowerbed[0] == 0 else 0
            return n <= 0
        previous, next = 0, flowerbed[1]
        for i in range(0, length):
            if (flowerbed[i] == 0 and previous == 0 and next == 0):
                n -= 1
                flowerbed[i] = 1
            previous = flowerbed[i]
            next = 0 if (i + 2 >= length) else flowerbed[i + 2]
        return n <= 0
