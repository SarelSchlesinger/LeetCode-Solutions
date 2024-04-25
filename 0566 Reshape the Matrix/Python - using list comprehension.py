class Solution(object):
    def matrixReshape(self, mat, r, c):
        matrix = [i for row in mat for i in row]
        return [matrix[i: i + c] for i in range(0, len(matrix), c)] if r * c == len(matrix) else mat