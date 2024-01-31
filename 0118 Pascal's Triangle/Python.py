class Solution(object):
    def generate(self, numRows):
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            lastRow = list(res[-1])
            currentRow = []
            while True:
                firstElem = lastRow.pop(0)
                if not lastRow:
                    break
                currentRow.append(firstElem + lastRow[0])
            res.append([1] + currentRow + [1])
        return res