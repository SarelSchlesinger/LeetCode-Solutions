# first approach - brute force
# time complexity: O(n^2)
# space complexity: O(1)

class Solution(object):
    def findMaxK(self, nums):
        res = -1
        for i in nums:
            for j in nums:
                if -i == j:
                    res = max(res, abs(i))
        return res

# second approach - two pointers
# time complexity: O(n*log(n))
# space complexity: O(n)

class Solution(object):
    def findMaxK(self, nums):
        nums.sort()    # using Timsort
        head = 0
        tail = len(nums) - 1
        while head < tail:
            if nums[head] > 0: return -1
            if nums[head] + nums[tail] == 0:
                return nums[tail]
            if nums[tail] > -nums[head]:
                tail -= 1
            else:
                head += 1
        return -1