# time complexity: O(n * log(n))
# space complexity: O(n)

class Solution(object):
    def minDifference(self, nums):
        if len(nums) <= 4: return 0
        nums.sort()
        res = float("inf")
        for i in range(4):
            res = min(res, nums[i + len(nums) - 4] - nums[i])
        return res