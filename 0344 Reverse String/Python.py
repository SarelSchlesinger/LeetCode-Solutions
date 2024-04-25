# two pointers approach
# time complexity: O(n)
# space complexity: O(1)
class Solution(object):
    def reverseString(self, s):
        head = 0
        tail = len(s) - 1
        while head < tail:
            s[head], s[tail] = s[tail], s[head]
            head += 1
            tail -= 1