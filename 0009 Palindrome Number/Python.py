class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        str_x = str(x)
        while True:
            if len(str_x) <= 1:
                return True
            if str_x[0] == str_x[-1]:
                str_x = str_x[1:-1]
            else:
                return False