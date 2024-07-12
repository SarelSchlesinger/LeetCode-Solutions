// time complexity: O(n)
// space complexity: O(n)

class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if (stack.empty()) {
                return false;
            } else {
                char ch = stack.top();
                stack.pop();
                if ((ch == '(' && c != ')') ||
                        (ch == '[' && c != ']') ||
                        (ch == '{' && c != '}')) return false;
            }
        }
        return stack.empty();
    }
};