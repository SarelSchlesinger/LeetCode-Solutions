// time Complexity: O(n)
// space complexity: O(1)

class Solution {
public:
    int firstUniqChar(string s) {
        int frequency[26];
        int index[26];
        for (int i = 0; i < 26; i++) {
            frequency[i] = 0;
            index[i] = -1;
        }
        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            frequency[c - 'a']++;
            index[c - 'a'] = i;  
        }
        int minNum = 100000;
        for (int i = 0; i < 26; i++) {
            if (frequency[i] == 1) {
                minNum = min(minNum, index[i]);
            }
        }
        return minNum == 100000 ? -1 : minNum;
    }
};