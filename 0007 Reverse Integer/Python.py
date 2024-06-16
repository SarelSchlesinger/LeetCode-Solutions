# time complexity: O(log(x))
# space complexity: O(1)

class Solution(object):
    def reverse(self, x):
        res = 0
        flag = False
        if x < 0:
            flag = True
            x = -x
        while x != 0:
            res *= 10
            res += x % 10
            x //= 10
        if flag:
            res = -res
        return 0 if res > pow(2, 31) - 1 or res < -pow(2, 31) else res