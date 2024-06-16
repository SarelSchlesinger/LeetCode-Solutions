# first approach - using stack
# time Complexity: O(n)
# space complexity: O(n)
class Solution(object):
    def isPalindrome(self, s):
        stack = list()
        for char in s:
            if char.isalnum():
                stack.append(char.lower())
        for char in s:
            if char.isalnum() and char.lower() != stack.pop():
                return False
        return True

# second approach - using two pointers
# time Complexity: O(n)
# space complexity: O(1)
class Solution(object):
    def isPalindrome(self, s):
        head = 0
        tail = len(s) - 1
        while head < tail:
            if not s[head].isalnum():
                head += 1
            elif not s[tail].isalnum():
                tail -= 1
            elif s[head].lower() != s[tail].lower(): 
                    return False
            else:
                head += 1
                tail -= 1
        return True