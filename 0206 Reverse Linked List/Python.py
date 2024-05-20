class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# first approach - iterative approach using stack
# time complexity: O(n)
# space complexity: O(n)
class Solution(object):
    def reverseList(self, head):
        if not head: return None
        stack = list()
        while head:
            stack.append(head)
            head = head.next
        newHead = tail = stack.pop()
        while stack:
            currentNode = stack.pop()
            tail.next = currentNode
            tail = currentNode
        tail.next = None
        return newHead

# second approach - iterative approach
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