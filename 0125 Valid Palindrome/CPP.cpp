// first approach - using stack
// time Complexity: O(n)
// space complexity: O(n)
class Solution {
public:
    bool isPalindrome(string s) {
        stack<char> stack;
        for (int i = 0; i < s.length(); i++) {
            if (isalpha(s[i]) || isdigit(s[i])) {
                stack.push(tolower(s[i]));
            }
        }
        for (int i = 0; i < s.length(); i++) {
            if (isalpha(s[i]) || isdigit(s[i])) {
                if (tolower(s[i]) != stack.top()) {
                    return false;
                }
                stack.pop();
            }
        }
        return true;
    }
};

// second approach - using two pointers
// time Complexity: O(n)
// space complexity: O(1)
class Solution {
public:
    bool isPalindrome(string s) {
        int head = 0;
        int tail = s.length() - 1;
        while (head < tail) {
            if (!isalpha(s[head]) && !isdigit(s[head])) {
                head++;
            } else if (!isalpha(s[tail]) && !isdigit(s[tail])) {
                tail--;
            } else if (tolower(s[head]) != tolower(s[tail])) { 
                return false;
            } else {
                head++;
                tail--;
            }
        }
        return true;
    }
};