# time complexity:  O(1)
# space complexity: O(1)

class Solution(object):
    def isPowerOfTwo(self, n):
        return False if n <= 0 else n & (n - 1) == 0