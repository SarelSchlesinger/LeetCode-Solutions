class Solution(object):
    def isMonotonic(self, nums):
        monotoneIncreasing = True
        monotoneDecreasing = True
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: continue
            elif nums[i] > nums[i - 1]:
                monotoneDecreasing = False
            else:
                monotoneIncreasing = False
            if not monotoneIncreasing and not monotoneDecreasing: return False
        return True