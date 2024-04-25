class Solution(object):
    def rearrangeArray(self, nums):
        res = [0] * len(nums)
        pos_index = 0
        neg_index = 1
        for num in nums:
            if num > 0:
                res[pos_index] = num
                pos_index += 2
            else:
                res[neg_index] = num
                neg_index += 2
        return res