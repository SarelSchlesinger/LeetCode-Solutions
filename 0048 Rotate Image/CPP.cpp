// time complexity: O(n^2)
// space complexity: O(1)

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        // transpose matrix
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = i; j < matrix.size(); j++) {
                if (i != j) {
                    swap(matrix[i][j], matrix[j][i]);
                }
            }
        }
        // reverse rows
        for (int i = 0; i < matrix.size(); i++) {
            int l = 0, r = matrix.size() - 1;
            while (l < r) {
                swap(matrix[i][l], matrix[i][r]);
                l += 1;
                r -= 1;
            }
        } 
    }
};