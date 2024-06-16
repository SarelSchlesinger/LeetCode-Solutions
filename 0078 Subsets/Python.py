# time complexity: O(n * 2^n)

class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for num in nums:
            subsets = list()
            for subset in res:
                subsets.append(subset + [num])
            res += subsets
        return res