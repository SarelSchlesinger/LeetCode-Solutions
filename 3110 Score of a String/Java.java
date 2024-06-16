// time complexity: O(n)
// space complexity: O(1)

class Solution {
    public int scoreOfString(String s) {
        int res = 0;
        for (int i = 1; i < s.length(); i++) {
            res += Math.abs((int) s.charAt(i - 1) - (int) s.charAt(i));
        }
        return res;
    }
}