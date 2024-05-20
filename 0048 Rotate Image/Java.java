// time complexity: O(n^2)
// space complexity: O(1)

class Solution {
    public void rotate(int[][] matrix) {
        // transpose matrix
        for (int i = 0; i < matrix.length; i++) {
            for (int j = i; j < matrix.length; j++) {
                if (i != j) {
                    matrix[i][j] += matrix[j][i];
                    matrix[j][i] = matrix[i][j] - matrix[j][i];
                    matrix[i][j] -= matrix[j][i];
                }
            }
        }
        // reverse rows
        for (int i = 0; i < matrix.length; i++) {
            int l = 0, r = matrix.length - 1;
            while (l < r) {
                matrix[i][l] += matrix[i][r];
                matrix[i][r] = matrix[i][l] - matrix[i][r];
                matrix[i][l] -= matrix[i][r];
                l += 1;
                r -= 1;
            }
        }
    }
}