# two pointers approach
# time complexity: O(n)
# space complexity: O(1)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeNodes(self, head):
        slow = head
        fast = head.next
        while fast:
            if fast.val != 0:
                slow.val += fast.val
            elif fast.next:
                slow.next = fast
                slow = slow.next
            else:
                slow.next = None
                break
            fast = fast.next
        return head