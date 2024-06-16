// using hashmap
// time Complexity: O(n)
// space complexity: O(n)

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        unordered_map<char, int> hmS;
        unordered_map<char, int> hmT;
        for (int i = 0; i < t.length(); i++) {
            hmS[s[i]]++;
            hmT[t[i]]++;
        }
        return hmS == hmT;
    }
};