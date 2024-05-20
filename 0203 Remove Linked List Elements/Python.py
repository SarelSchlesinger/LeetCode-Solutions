# time complexity: O(n)
# space complexity: O(1)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeElements(self, head, val):
        prevNode = None
        currentNode = head
        while currentNode:
            if currentNode.val == val:
                if prevNode:
                    prevNode.next = currentNode.next
                else:
                    head = currentNode.next
            else:
                prevNode = currentNode
            currentNode = currentNode.next
        return head
        