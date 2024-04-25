# time complexity: O(n)
# space complexity: O(1)

class Solution(object):
    def maxDepth(self, s):
        res = counter = 0
        for i in s:
            if i == '(':
                counter += 1
                if counter > res:
                    res = counter
            elif i == ')':
                counter -= 1
        return res