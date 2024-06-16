// using hashmap
// time Complexity: O(n)
// space complexity: O(1)

class Solution {
public:
    int longestPalindrome(string s) {
        int res = 0;
        bool flag = false;
        unordered_map<char, int> hm;
        for (int i = 0; i < s.length(); i++) {
            hm[s[i]]++;
        }
        for (auto it = hm.begin(); it != hm.end(); it++) {
            int num = it->second;
            if (num % 2 == 0) {
                res += num;
            } else {
                flag = true;
                res += num - 1;
            }
        }
        return flag ? res + 1 : res;
    }
};