// first approach - using stack
// time Complexity: O(n)
// space complexity: O(n)
class Solution {
    public boolean isPalindrome(String s) {
        List<Character> stack = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isLetterOrDigit(c)) {
                stack.add(Character.toLowerCase(c));
            }
        }
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isLetterOrDigit(c) && Character.toLowerCase(c) != stack.remove(stack.size() - 1)) {
                return false;
            }
        }
        return true;
    }
}

// second approach - using two pointers
// time Complexity: O(n)
// space complexity: O(1)
class Solution {
    public boolean isPalindrome(String s) {
        int head = 0;
        int tail = s.length() - 1;
        while (head < tail) {
            if (!Character.isLetterOrDigit(s.charAt(head))) {
                head++;
            } else if (!Character.isLetterOrDigit(s.charAt(tail))) {
                tail--;
            } else if (Character.toLowerCase(s.charAt(head)) != Character.toLowerCase(s.charAt(tail))) { 
                return false;
            } else {
                head++;
                tail--;
            }
        }
        return true;
    }
}