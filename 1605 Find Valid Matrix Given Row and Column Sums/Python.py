# time complexity: O(m * n)
# space complexity: O(m * n)

class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        mat = [[0] * len(colSum) for _ in range(len(rowSum))]
        for rowIndex in range(len(rowSum)):
            for colIndex in range(len(colSum)):
                mat[rowIndex][colIndex] = min(rowSum[rowIndex], colSum[colIndex])
                rowSum[rowIndex] -= mat[rowIndex][colIndex]
                colSum[colIndex] -= mat[rowIndex][colIndex]
        return mat