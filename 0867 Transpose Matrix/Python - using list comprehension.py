# using list comprehension
# time complexity: O(n*m)
# space complexity: O(n*m)

class Solution(object):
    def transpose(self, matrix):
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]