class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        while len(nums) > 2:
            if sum(nums[:-1]) <= nums[-1]:
                del nums[-1]
            else:
                return sum(nums)
        return -1