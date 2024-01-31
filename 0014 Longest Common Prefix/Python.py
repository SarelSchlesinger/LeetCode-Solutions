class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""
        for i in range(len(min(strs))):
            j = [word[i] for word in strs]
            if len(set(j)) > 1:
                return res
            res += j[0]
        return res