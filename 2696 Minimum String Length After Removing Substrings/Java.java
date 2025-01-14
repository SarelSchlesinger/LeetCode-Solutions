// time complexity:  O(n)
// space complexity: O(n)

class Solution {
    public int minLength(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (!stack.isEmpty() && ((stack.peek() == 'A' && s.charAt(i) == 'B') || (stack.peek() == 'C' && s.charAt(i) == 'D'))) {
                stack.pop();
            } else {
                stack.push(s.charAt(i));
            }
        }
        return stack.size();
    }
}