# using hashmap
# time Complexity: O(n)
# space complexity: O(1)

class Solution(object):
    def longestPalindrome(self, s):
        res = 0
        flag = False
        for i in Counter(s).values():
            if i % 2 == 0:
                res += i
            else:
                flag = True
                res += i - 1
        return res + 1 if flag else res