// time complexity: O(n)
// space complexity: O(1)
class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int diagonalsSum = 0;
        int i = 0;
        while (i < mat.size()) {
            if (i != mat.size() - 1 - i) {
                diagonalsSum += mat[i][i] + mat[i][mat.size() - 1 - i];
            }
            else {
                diagonalsSum += mat[i][i];
            }
            i += 1;
        }
        return diagonalsSum;
    }
};