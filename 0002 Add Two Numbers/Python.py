class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = ListNode()
        currentNode = head
        while True:
            if l1 and l2:
                if l1.val + l2.val + carry < 10:
                    currentNode.val = l1.val + l2.val + carry
                    carry = 0
                else:
                    currentNode.val = (l1.val + l2.val + carry) % 10
                    carry = 1
                l1 = l1.next
                l2 = l2.next
            elif l1 or l2:
                if l1:
                    if l1.val + carry < 10:
                        currentNode.val = l1.val + carry
                        carry = 0
                    else:
                        currentNode.val = (l1.val + carry) % 10
                        carry = 1
                    l1 = l1.next
                else:
                    if l2.val + carry < 10:
                        currentNode.val = l2.val + carry
                        carry = 0
                    else:
                        currentNode.val = (l2.val + carry) % 10
                        carry = 1
                    l2 = l2.next
            if not l1 and not l2:
                break
            currentNode.next = ListNode()
            currentNode = currentNode.next
        
        if carry == 1:
            currentNode.next = ListNode(1)

        return head