# using hashmap
# time Complexity: O(n)
# space complexity: O(n)

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): return False
        return Counter(s) == Counter(t)