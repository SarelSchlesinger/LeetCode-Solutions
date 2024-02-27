# runtime complexity: O(n)
# space complexity: O(1)

class Solution(object):
    def missingNumber(self, nums):
        return sum(range(len(nums))) - (sum(nums) - len(nums))