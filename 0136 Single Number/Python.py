# time complexity: O(n)
# space complexity: O(1)

class Solution(object):
    def singleNumber(self, nums):
        return reduce(lambda a, b: a ^ b, nums)