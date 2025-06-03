// time complexity:  O(1)
// space complexity: O(1)

class Solution {
    public long coloredCells(int n) {
        return (long) 2 * n * (n - 1) + 1;
    }
}