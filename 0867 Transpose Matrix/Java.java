// time complexity:  O(m * n)
// space complexity: O(m * n)

class Solution {
    public int[][] transpose(int[][] matrix) {
        int[][] new_matrix = new int[matrix[0].length][matrix.length];
        for (int i = 0; i < new_matrix.length; i++) {
            for (int j = 0; j < new_matrix[0].length; j++) {
                    new_matrix[i][j] = matrix[j][i];
            }
        }
        return new_matrix;
    }
}