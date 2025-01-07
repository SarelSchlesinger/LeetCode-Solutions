# time complexity:  O(n)
# space complexity: O(n)

class Solution(object):
    def minLength(self, s):
        stack = list()
        for char in s:
            if len(stack) > 0 and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                stack.pop()
            else:
                stack.append(char)
        return len(stack)