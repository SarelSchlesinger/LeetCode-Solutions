# two pointers approach
# time complexity: O(n)
# space Complexity : O(n)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reorderList(self, head):
        L = list()
        while head:
            L.append(head)
            head = head.next
        head = 0
        tail = len(L) - 1
        while head < tail:
            L[head].next = L[tail]
            head += 1
            L[tail].next = L[head]
            tail -= 1
        L[head].next = None