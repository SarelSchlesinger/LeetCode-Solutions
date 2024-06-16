// using two pointers
// time Complexity: O(n)
// space complexity: O(1)

class Solution {
    public int appendCharacters(String s, String t) {
        int i = 0, j = 0;
        while (j < t.length() && i < s.length()) {
            if (t.charAt(j) == s.charAt(i)) {
                j++;
            }
            i++;
        }
        return t.length() - j;
    }
}