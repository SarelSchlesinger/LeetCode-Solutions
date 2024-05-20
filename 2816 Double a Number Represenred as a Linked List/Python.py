class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# first approach - using stack
# time complexity: O(n)
# space complexity: O(n)
class Solution(object):
    def doubleIt(self, head):
        stack = list()
        while head:
            stack.append(head)
            head = head.next
        carry = 0
        for i in range(len(stack) - 1, -1, -1):
            if stack[i].val > 4:
                stack[i].val = (stack[i].val * 2 + carry) % 10
                carry = 1
            else:
                stack[i].val = stack[i].val * 2 + carry
                carry = 0
        return stack[0] if not carry else ListNode(1, stack[0])

# first approach - reverse twice
# time complexity: O(n)
# space complexity: O(1)
class Solution(object):

    def reverse(self, head):
        prevNode, nextNode = None, None
        while head:
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode
        return prevNode

    def doubleIt(self, head):
        # first reverse
        newHead = self.reverse(head)
        tail = newHead
        carry = 0
        while newHead:
            if newHead.val > 4:
                newHead.val = (newHead.val * 2 + carry) % 10
                carry = 1
            else:
                newHead.val = newHead.val * 2 + carry
                carry = 0
            newHead = newHead.next
        # second reverse
        head = self.reverse(tail)
        return head if not carry else ListNode(1, head)

# third approach - two pointers
# time complexity: O(n)
# space complexity: O(1)
class Solution(object):
    def doubleIt(self, head):
        prevNode = None
        currentNode = head
        if head.val > 4:
            prevNode = head = ListNode(0, currentNode)
        while currentNode:
            if currentNode.val > 4:
                prevNode.val += 1
            currentNode.val = (currentNode.val * 2) % 10
            prevNode = currentNode
            currentNode = currentNode.next
        return head

# fourth approach - single pointer
# time complexity: O(n)
# space complexity: O(1)
class Solution(object):
    def doubleIt(self,head):
        currentNode = head
        if head.val > 4:
            head = ListNode(1, currentNode)
        while currentNode:
            currentNode.val = (currentNode.val * 2) % 10
            if currentNode.next and currentNode.next.val > 4:
                currentNode.val += 1
            currentNode = currentNode.next
        return head