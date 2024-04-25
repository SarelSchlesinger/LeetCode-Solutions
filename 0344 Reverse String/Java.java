// two pointers approach
// time complexity: O(n)
// space complexity: O(1)

class Solution {
    public void reverseString(char[] s) {
        int head = 0;
        int tail = s.length - 1;
        while (head < tail) {
            char temp;
            temp = s[head];
            s[head] = s[tail];
            s[tail] = temp;
            head++;
            tail--;
        }
    }
}