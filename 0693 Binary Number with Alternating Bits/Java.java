// time complexity:  O(1)
// space complexity: O(1)

class Solution {
    public boolean hasAlternatingBits(int n) {
        String bin = Integer.toBinaryString(n);
        for (int i = 1 ; i < bin.length() ; i++) {
            if (bin.charAt(i) == bin.charAt(i - 1)) return false;
        }
        return true;
    }
}