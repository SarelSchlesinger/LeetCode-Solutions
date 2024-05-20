class Solution(object):
    
    def powerset(self, nums):
        res = [[]]
        for i in nums:
            new_subsets = list()
            for subset in res:
                new_subsets.append(subset + [i])
            res += new_subsets
        return res
    
    def subsetXORSum(self, nums):
        res = 0
        for subset in self.powerset(nums):
            subset_res = 0
            for i in subset:
                subset_res ^= i
            res += subset_res
        return res