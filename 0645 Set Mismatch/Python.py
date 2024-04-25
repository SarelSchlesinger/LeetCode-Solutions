class Solution(object):
    def findErrorNums(self, nums):
        d = dict()
        for i in range(len(nums)):
            d[i + 1] = 0
        for i in nums:
            d[i] += 1
        sorted_d = sorted(d.items(), key=lambda x:x[1])
        return [sorted_d[-1][0], sorted_d[0][0]]