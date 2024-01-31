class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None and list2 is None:
            return None
        root = ListNode()
        currentNode = root
        while True:
            if list1 and not list2:
                currentNode.val = list1.val
                list1 = list1.next
                if not list1:
                    break
            elif not list1 and list2:
                currentNode.val = list2.val
                list2 = list2.next
                if not list2:
                    break
            elif list1.val < list2.val:
                currentNode.val = list1.val
                list1 = list1.next
            else:
                currentNode.val = list2.val
                list2 = list2.next
            currentNode.next = ListNode()
            currentNode = currentNode.next
        return root