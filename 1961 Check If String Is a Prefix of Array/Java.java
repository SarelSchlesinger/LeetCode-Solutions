// time complexity:  O(m * n)
// space complexity: O(1)

class Solution {
    public boolean isPrefixString(String s, String[] words) {
        int i = 0;
        for (String word : words) {
            for (int j = 0 ; j < word.length() ; j++) {
                if (s.charAt(i) != word.charAt(j)) return false;
                if (++i == s.length()) {
                    return j == word.length() - 1 ? true : false;
                }
            }
        }
        return false;
    }
}