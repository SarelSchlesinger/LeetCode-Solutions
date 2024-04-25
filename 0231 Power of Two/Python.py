class Solution(object):
    def isPowerOfTwo(self, n):
        return True if bin(n)[2] == '1' and '1' not in bin(n)[3:] else False