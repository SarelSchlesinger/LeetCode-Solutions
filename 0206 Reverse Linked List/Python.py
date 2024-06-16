class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# first approach - using stack
# time complexity: O(n)
# space complexity: O(n)
class Solution(object):
    def reverseList(self, head):
        if not head: return None
        stack = list()
        while head:
            stack.append(head)
            head = head.next
        for i in range(1, len(stack)):
            stack[i].next = stack[i - 1]
        stack[0].next = None
        return stack[-1]

# second approach - using two pointers
# time complexity: O(n)
# space complexity: O(1)
class Solution(object):
    def reverseList(self, head):
        if not head: return None
        prevNode = None
        nextNode = None
        while head:
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode
        return prevNode