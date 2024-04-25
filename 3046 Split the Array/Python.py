# time complexity: O(n)
# space complexity: O(n)
class Solution(object):
    def isPossibleToSplit(self, nums):
        return not max(Counter(nums).values()) > 2


# time complexity: O(n)
# space complexity: O(1)
class Solution(object):
    def isPossibleToSplit(self, nums):
        counter = [0] * 101
        for i in nums:
            if counter[i] == 2:
                return False
            else:
                counter[i] += 1
        return True
        