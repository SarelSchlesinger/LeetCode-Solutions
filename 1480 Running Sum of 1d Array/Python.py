class Solution(object):
    def runningSum(self, nums):
        L = []
        for num in range(1, len(nums) + 1):
            L.append(sum(nums[:num]))
        return L