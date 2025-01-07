# time complexity:  O(log(n))
# space complexity: O(1)

class Solution(object):
    def firstBadVersion(self, n):
        l, r = 1, n
        while l < r:
            middle = (l + r ) // 2
            if isBadVersion(middle):
                r = middle
            else:
                l = middle + 1
        return r