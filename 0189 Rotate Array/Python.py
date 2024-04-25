# time complexity: O(n)
# space complexity: O(n)
class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        
# time complexity: O(n)
# space complexity: O(n)
class Solution(object):
    def rotate(self, nums, k):
        newNums = nums[:]
        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = newNums[i]
            
# time complexity: O(n)
# space complexity: O(1)
class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        # reverse head
        i = 0
        j = len(nums) - (k + 1)
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        # reverse tail
        i = len(nums) - k
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        # reverse all            
        i = 0
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1