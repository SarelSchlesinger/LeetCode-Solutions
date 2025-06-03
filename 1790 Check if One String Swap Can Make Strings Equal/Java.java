// time complexity:  O(1) (Constraints: 1 <= s1.length, s2.length <= 100)
// space complexity: O(1)

class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        int[] freq = new int[26];
        int difference = 0;
        for (int i = 0; i < s1.length(); i++) {
            freq[s1.charAt(i) - 'a']++;
            freq[s2.charAt(i) - 'a']--;
            if (s1.charAt(i) != s2.charAt(i)) {
                if (++difference > 2) return false;
            }
        }
        for (int j : freq) {
            if (j != 0) return false;
        }
        return !(difference == 1);
    }
}