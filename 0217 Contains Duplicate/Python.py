# first approach - using set
# time complexity: O(n)
# space complexity: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


# second approach - using sorting
# time complexity: O(n*log(n))
# space complexity: O(1)       
class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: return True
        return False