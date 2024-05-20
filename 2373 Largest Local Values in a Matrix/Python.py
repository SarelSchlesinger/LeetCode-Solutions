# time complexity: O(n^2)
# space complexity: O(n^2)

class Solution(object):
    def largestLocal(self, grid):
        maxLocal = [[0 for _ in range(len(grid) - 2)] for _ in range(len(grid) - 2)]
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid) - 1):
                maxLocal[i - 1][j - 1] = max(grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1], grid[i][j - 1], grid[i][j], grid[i][j + 1], grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1])
        return maxLocal