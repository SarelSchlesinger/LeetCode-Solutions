class Solution(object):
    def construct2DArray(self, original, m, n):
        return [] if m * n != len(original) else [original[i: i + n] for i in range(0, len(original), n)]