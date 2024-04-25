# Dynamic Programming Approach

class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        stairs = [0] * (n + 1)
        stairs[1] = 1
        stairs[2] = 2
        for i in range(3, n + 1):
            stairs[i] = stairs[i - 1] + stairs[i - 2]
        return stairs[n]