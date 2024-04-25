# two pointers approach
# time complexity: O(n)
# space complexity: O(1)

class Solution(object):
    def moveZeroes(self, nums):
        i = j = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1
        for k in range(j, len(nums)):
            nums[k] = 0