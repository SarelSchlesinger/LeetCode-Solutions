class Solution(object):
    def customSortString(self, order, s):
        res = str()
        for letter in order:
            if letter in s:
                length = len(s)
                s = s.replace(letter, '')
                res += letter * (length - len(s))
        return res + s