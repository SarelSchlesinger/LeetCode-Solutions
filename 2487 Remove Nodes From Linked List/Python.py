class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# first approach - using stack
# time complexity: O(n)
# space complexity: O(n)
class Solution(object):
    def removeNodes(self, head):
        stack = []
        while head:
            stack.append(head)
            head = head.next
        newHead = stack.pop() 
        while stack:
            currentNode = stack.pop()
            if currentNode.val >= newHead.val:
                currentNode.next = newHead
                newHead = currentNode
        return newHead
        
# second approach - reverse twice
# time complexity: O(n)
# space complexity: O(1)
class Solution(object):

    def reverse(self, head):
        prevNode = nextNode = None
        while head:
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode
        return prevNode

    def removeNodes(self, head):
        # first reverse
        newHead = self.reverse(head)
        # remove nodes
        head = newHead
        while newHead.next:
            if newHead.val > newHead.next.val:
                newHead.next = newHead.next.next
            else:
                newHead = newHead.next
        # second reverse
        return self.reverse(head)