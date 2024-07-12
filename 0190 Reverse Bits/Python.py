# time complexity: O(1)
# space complexity: O(1)

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            if n & 1:
                res += pow(2, 31 - i) 
            n >>= 1
        return res