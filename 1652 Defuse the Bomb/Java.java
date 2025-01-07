// time complexity:  O(n * |k|)
// space complexity: O(n)

class Solution {
    public int[] decrypt(int[] code, int k) {
        int[] res = new int[code.length];
        if (k == 0) return res;
        for (int i = 0; i < code.length; i++) {
            if (k > 0) {
                for (int j = 1; j <= k; j++) {
                    res[i] += code[(i + j) % code.length];
                }
            } else {
                for (int j = 1; j <= -k; j++) {
                    res[i] += code[(i - j + code.length) % code.length];
                }
            }
        }
        return res;
    }
}