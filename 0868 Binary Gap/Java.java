// time complexity:  O(1)
// space complexity: O(1)

class Solution {
    public int binaryGap(int n) {
        int res = 0;
        String bin = Integer.toBinaryString(n);
        int prev = bin.indexOf("1");
        for (int i = prev + 1 ; i < bin.length() ; i++) {
            if (bin.charAt(i) == '1') {
                res = Math.max(res, i - prev);
                prev = i;
            }
        }
        return res;
    }
}