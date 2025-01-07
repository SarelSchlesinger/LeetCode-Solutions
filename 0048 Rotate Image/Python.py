# time complexity:  O(n^2)
# space complexity: O(1)

def rotate(self, matrix):
        # transpose matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]        
        # reverse rows
        for row in matrix:
            l = 0
            r = len(matrix) - 1
            while l < r:
                row[l], row[r] = row[r], row[l]
                l += 1
                r -= 1