# time complexity: O(n^2)
# space complexity: O(1)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    
    def reversedLinkedList(self, head):
        prevNode = nextNode = None
        while head:
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode
        return prevNode
    
    def isPalindrome(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tail = self.reversedLinkedList(slow)
        while tail:
            if tail.val != head.val: return False
            tail = tail.next
            head = head.next
        return True