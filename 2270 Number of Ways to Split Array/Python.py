# time complexity:  O(n)
# space complexity: O(1)

class Solution(object):
    def waysToSplitArray(self, nums):
        total_sum = sum(nums)
        current_sum = 0
        res = 0
        for i in range(len(nums) - 1):
            current_sum += nums[i]
            if current_sum >= total_sum - current_sum:
                res += 1
        return res