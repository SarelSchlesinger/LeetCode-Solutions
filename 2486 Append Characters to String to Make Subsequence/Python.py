# using two pointers
# time Complexity: O(n)
# space complexity: O(1)

class Solution(object):
    def appendCharacters(self, s, t):
        i = j = 0
        while j < len(t) and i < len(s):
            if t[j] == s[i]:
                j += 1
            i += 1
        return len(t) - j