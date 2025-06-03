# time complexity:  O(n)
# space complexity: O(n)

class Solution(object):
    def shuffle(self, nums, n):
        new_nums = [0] * 2 * n
        for i in range(n):
            new_nums[i * 2] += nums[i]
            new_nums[i * 2 + 1] += nums[i + n]
        return new_nums
        