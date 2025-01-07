// time complexity:  O(m * n^2)
// space complexity: O(m * n)

class Solution {
    public char[][] rotateTheBox(char[][] box) {
        int m = box.length, n = box[0].length;
        char[][] rotated_box = new char[n][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rotated_box[j][m - 1 - i] = box[i][j];
            }
        }
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < m; j++) {
                if (rotated_box[i][j] == '#' && rotated_box[i + 1][j] == '.') {
                    int k = i + 1;
                    while (k + 1 < n && rotated_box[k + 1][j] == '.') {
                        k++;
                    }
                    rotated_box[i][j] = '.';
                    rotated_box[k][j] = '#';
                }
            }
        }
        return rotated_box;
    }
}