# Time Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        d = dict()
        for index, value in enumerate(nums):
            if target - value in d:
                return [d[target - value], index]
            else:
                d[value] = index