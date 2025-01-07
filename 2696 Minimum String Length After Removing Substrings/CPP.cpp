// time complexity:  O(n)
// space complexity: O(n)

class Solution {
public:
    int minLength(string s) {
        stack<char> stack;
        for (int i = 0; i < s.length(); i++) {
            if (!stack.empty() && ((stack.top() == 'A' && s[i] == 'B') || (stack.top() == 'C' && s[i] == 'D'))) {
                stack.pop();
            } else {
                stack.push(s[i]);
            }
        }
        return stack.size();
    }
};