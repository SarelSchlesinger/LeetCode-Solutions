# time complexity:  O(max(m, n))
# space complexity: O(1)

class Solution(object):
    def minBitFlips(self, start, goal):
        xor_res = start ^ goal
        counter = 0
        while xor_res:
            counter += xor_res & 1
            xor_res >>= 1
        return counter