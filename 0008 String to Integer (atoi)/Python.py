# time complexity: O(n)

class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        if not s: return 0
        neg = -1 if s[0] == "-" else 1
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        s = ''.join(takewhile(lambda ch: ch.isdigit(), s))
        if not s: return 0
        s = neg * int(s)
        MaxNum = pow(2, 31) - 1
        MinMum = -pow(2, 31)
        if s > MaxNum: return MaxNum
        if s < MinMum: return MinMum
        return s