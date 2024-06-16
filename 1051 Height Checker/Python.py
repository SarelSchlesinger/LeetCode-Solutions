# time Complexity: O(n * log(n))
# space complexity: O(n)

class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        return res