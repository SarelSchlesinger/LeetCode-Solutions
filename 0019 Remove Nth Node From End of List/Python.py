class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# first approach - using stack
# time complexity: O(n)
# space complexity: O(n)
class Solution(object):
    def removeNthFromEnd(self, head, n):
        stack = list()
        while head:
            stack.append(head)
            head = head.next
        if len(stack) == 1:
            return None
        elif n == 1:
            stack[-2].next = None
        elif n == len(stack):
            return stack[1]
        else:
            stack[-(n + 1)].next = stack[-(n - 1)]
        return stack[0]

# second approach - using two pointers
# time complexity: O(n)
# space complexity: O(1)
class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head