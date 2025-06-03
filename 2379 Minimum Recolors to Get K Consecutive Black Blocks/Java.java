// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public int minimumRecolors(String blocks, int k) {
        int w_blocks = 0;
        for (int i = 0 ; i < k ; i++) {
            if (blocks.charAt(i) == 'W') w_blocks++;
        }
        int res = w_blocks;
        for (int i = 1 ; i <= blocks.length() - k ; i++) {
            if (blocks.charAt(i - 1) == 'W') w_blocks--;
            if (blocks.charAt(i + k - 1) == 'W') w_blocks++;
            res = Math.min(res, w_blocks);
        }
        return res;
    }
}