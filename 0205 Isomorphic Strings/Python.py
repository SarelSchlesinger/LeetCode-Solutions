# using hashmap
# time complexity: O(n)
# space complexity: O(n)
class Solution(object):
    def isIsomorphic(self, s, t):
        hashmapS, hashmapT = dict(), dict()
        for i in range(len(s)):
            if s[i] not in hashmapS:
                hashmapS[s[i]] = t[i]
            elif hashmapS[s[i]] != t[i]: return False

            if t[i] not in hashmapT:
                hashmapT[t[i]] = s[i]
            elif hashmapT[t[i]] != s[i]: return False
        return True