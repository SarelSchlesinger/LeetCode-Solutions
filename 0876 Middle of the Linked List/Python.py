class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def middleNode(self, head):
        L = [head]
        while head.next:
            L.append(head.next)
            head = head.next
        return L[len(L)/2]