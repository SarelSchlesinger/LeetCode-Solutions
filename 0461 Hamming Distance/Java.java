// time complexity: O(log(n))
// space complexity: O(1)

class Solution {
    public int hammingDistance(int x, int y) {
        int z = x ^ y;
        int res = 0;
        while (z > 0) {
            res += z & 1;
            z >>= 1;
        }
        return res;
    }
}