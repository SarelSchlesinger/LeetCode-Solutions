// time complexity:  O(max(m, n))
// space complexity: O(1)

class Solution {
    public int minBitFlips(int start, int goal) {
        int xor_res = start ^ goal;
        int counter = 0;
        while (xor_res > 0) {
            counter += xor_res & 1;
            xor_res >>= 1;
        }
        return counter;
    }
}