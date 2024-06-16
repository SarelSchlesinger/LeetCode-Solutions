// using two pointers
// time Complexity: O(n)
// space complexity: O(1)

class Solution {
public:
    int appendCharacters(string s, string t) {
        int i = 0, j = 0;
        while (j < t.length() && i < s.length()) {
            if (t[j] == s[i]) {
                j++;
            }
            i++;
        }
        return t.length() - j;
    }
};