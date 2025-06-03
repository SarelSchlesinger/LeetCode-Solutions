// time complexity:  O(n^2)
// space complexity: O(n^2)

class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int[] freq = new int[grid.length * grid.length];
        for (int i = 0 ; i < grid.length ; i++) {
            for (int j = 0 ; j < grid.length ; j++) {
                freq[grid[i][j] - 1]++;
            }
        }
        int[] res = new int[2];
        for (int i = 0 ; i < freq.length ; i++) {
            if (freq[i] == 2) res[0] = i + 1;
            else if (freq[i] == 0) res[1] = i + 1;
        }
        return res;
    }
}