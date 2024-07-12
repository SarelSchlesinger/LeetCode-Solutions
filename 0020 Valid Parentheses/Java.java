// time complexity: O(n)
// space complexity: O(n)

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if (stack.empty()) {
                return false;
            } else {
                char ch = stack.pop();
                if ((ch == '(' && c != ')') ||
                        (ch == '[' && c != ']') ||
                        (ch == '{' && c != '}')) return false;
            }
        }
        return stack.empty();
    }
}