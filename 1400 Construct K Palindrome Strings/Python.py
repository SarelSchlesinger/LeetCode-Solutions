# time complexity:  O(n)
# space complexity: O(1)

class Solution(object):
    def canConstruct(self, s, k):
        if k > len(s): return False
        if k == len(s): return True
        return sum(v % 2 for v in Counter(s).values()) <= k