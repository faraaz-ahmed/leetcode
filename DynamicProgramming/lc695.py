class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_ = 0
        for y in range(0, len(grid)):
            for x in range(0, len(grid[0])):
                if grid[y][x] == 0 or grid[y][x] == 2:
                    grid[y][x] = 2
                else:
                    islandArea = self.returnAdjacentSquares(grid, y, x)
                    if islandArea > max_:
                        max_ = islandArea
        return max_
    def returnAdjacentSquares(self, grid, i, j):
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
            if grid[i][j] == 1:
                grid[i][j] = 2
                return 1 + self.returnAdjacentSquares(grid, i + 1, j) + self.returnAdjacentSquares(grid, i, j + 1) + self.returnAdjacentSquares(grid, i - 1, j) + self.returnAdjacentSquares(grid, i, j - 1)
            else:
                grid[i][j] = 2
                return 0
        return 0

test = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid2 = [[0,0,0,0,0,0,0,0]]
print(test.maxAreaOfIsland(grid))
print(test.maxAreaOfIsland(grid2))