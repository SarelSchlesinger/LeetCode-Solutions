// using hashmap
// time complexity: O(n)
// space complexity: O(n)
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> hashmapS;
        unordered_map<char, char> hashmapT;
        for (int i = 0; i < s.size(); i++) {
            if (!hashmapS.contains(s.at(i))) {
                hashmapS.insert({s.at(i), t.at(i)});
            } else if (hashmapS[s[i]] != t.at(i)) {
                return false;
            }
            if (!hashmapT.contains(t.at(i))) {
                hashmapT.insert({t.at(i), s.at(i)});
            } else if (hashmapT[t[i]] != s.at(i)) {
                return false;
            }
        }
        return true;
    }
};