# time complexity: O(n * log(n))
# space complexity: O(n)

class Solution(object):
    def minIncrementForUnique(self, nums):
        moves = 0
        nums.sort()
        i = 0
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                inc = nums[i] - nums[i + 1] + 1
                nums[i + 1] += inc
                moves += inc
        return moves