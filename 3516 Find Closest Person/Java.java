// time complexity:  O(1)
// space complexity: O(1)

class Solution {
    public int findClosest(int x, int y, int z) {
        return Math.abs(z - x) == Math.abs(z - y) ? 0 : (Math.abs(z - x) > Math.abs(z - y) ? 2 : 1);
    }
}