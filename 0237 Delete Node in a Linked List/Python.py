# time complexity: O(1)
# space complexity: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next