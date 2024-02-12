class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# first approach
class Solution(object):
    def reverseList(self, head):
        if not head: return None
        newHead = ListNode(head.val)
        while head.next:
            newNode = ListNode(head.next.val, newHead)
            newHead = newNode
            head = head.next 
        return newHead
        
# second approach - overrides the original linked list
class Solution(object):
    def reverseList(self, head):
        if not head: return None
        L = list()
        while head:
            L.append(head)
            head = head.next
            if len(L) == 1:
                L[0].next = None
            else:
                L[-1].next = L[-2]
        return L[-1]
