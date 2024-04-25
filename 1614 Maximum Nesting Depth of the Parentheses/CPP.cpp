// time complexity: O(n)
// space complexity: O(1)

class Solution {
public:
    int maxDepth(string s) {
        int res = 0, counter = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                counter++;
                if (counter > res) {
                    res = counter;
                }
            } else if (s[i] == ')') {
                counter--;
                }
        }
        return res;        
    }
};