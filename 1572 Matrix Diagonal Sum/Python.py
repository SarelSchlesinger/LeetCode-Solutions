# time complexity: O(n)
# space complexity: O(1)
class Solution(object):
    def diagonalSum(self, mat):
        diagonalsSum = 0
        for i in range(len(mat)):
            if i != len(mat) - 1 - i:
                diagonalsSum += mat[i][i] + mat[i][len(mat) - 1 - i]
            else:
                diagonalsSum += mat[i][i]
        return diagonalsSum