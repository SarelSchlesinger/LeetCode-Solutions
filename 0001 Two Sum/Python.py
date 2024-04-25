# first approach - brute force
# time Complexity: O(n^2)
# space complexity: O(1)
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# second approach - using hashmap
# time Complexity: O(n)
# space complexity: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        d = dict()
        for index, value in enumerate(nums):
            if target - value in d:
                return [d[target - value], index]
            else:
                d[value] = index