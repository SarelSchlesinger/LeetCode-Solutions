# time complexity: O(log(n))
# space complexity: O(1)

class Solution(object):
    def hammingDistance(self, x, y):
        z = x ^ y
        res = 0
        while z > 0:
            res += z & 1
            z >>= 1
        return res