// time complexity:  O(n)
// space complexity: O(1)

class Solution {
    public boolean isBalanced(String num) {
        int res = 0;
        for (int i = 0; i < num.length(); i++) {
            if (i % 2 == 0) {
                res += num.charAt(i) - '0';
            } else {
                res -= num.charAt(i) - '0';
            }
        }
        return res == 0;
    }
}