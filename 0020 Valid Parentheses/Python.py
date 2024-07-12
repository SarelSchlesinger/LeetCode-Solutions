# time complexity: O(n)
# space complexity: O(n)

class Solution(object):
    def isValid(self, s):
        stack = list()
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            elif not stack: return False
            else:
                last = stack.pop()
                if not ((i == ')' and last == '(') or (i == ']' and last == '[') or (i == '}' and last == '{')):
                    return False
        return not stack