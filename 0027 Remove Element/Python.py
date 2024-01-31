class Solution(object):
    def removeElement(self, nums, val):
        available = -1
        res = len(nums)
        for i in range(len(nums)):
            if nums[i] == "_":
                break
            while nums[i] == val:
                nums[i], nums[available] = nums[available], "_"
                res -= 1
                available -= 1
        return res