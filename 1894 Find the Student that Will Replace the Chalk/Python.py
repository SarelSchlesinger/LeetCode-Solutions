# time complexity: O(n)
# space complexity: O(1)

class Solution(object):
    def chalkReplacer(self, chalk, k):
        k %= sum(chalk)
        for i in range(len(chalk)):
            if k >= chalk[i]:
                k -= chalk[i]
            else:
                return i