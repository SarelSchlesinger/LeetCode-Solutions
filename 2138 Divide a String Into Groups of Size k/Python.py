class Solution(object):
    def divideString(self, s, k, fill):
        res = []
        i = 0
        while i < len(s) - len(s) % k:
            res.append(s[i: i + k])
            i += k
        if (i < len(s)):
           res.append(s[i:].ljust(k, fill))  
        return res