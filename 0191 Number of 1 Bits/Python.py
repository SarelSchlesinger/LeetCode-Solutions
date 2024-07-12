# time complexity: O(log(n))
# space complexity: O(1)

class Solution(object):
    def hammingWeight(self, n):
        res = 0
        while n > 0:
            if n % 2 == 1:
                res += 1
            n /= 2
        return res