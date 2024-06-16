# time Complexity: O(n)
# space complexity: O(1)

class Solution(object):
    def sortColors(self, nums):
        red = white = blue = 0
        for i in nums:
            if i == 0:
                red += 1
            elif i == 1:
                white += 1
            else:
                blue += 1
        for i in range(len(nums)):
            if red > 0:
                nums[i] = 0
                red -= 1
            elif white > 0:
                nums[i] = 1
                white -= 1
            else:
                nums[i] = 2