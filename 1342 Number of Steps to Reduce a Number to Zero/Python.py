class Solution(object):
    def numberOfSteps(self, num):
        res = 0
        while num > 0:
            if num % 2 == 0:
                res += 1
                num /= 2
            else:
                res += 1
                num -= 1
        return res