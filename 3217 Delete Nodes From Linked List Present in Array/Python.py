# time complexity: O(m + n)
# space complexity: O(m)

class Solution(object):
    def modifiedList(self, nums, head):
        nums = set(nums)
        currentNode = head
        head = prevNode = ListNode(0, head)
        while currentNode:
            if currentNode.val in nums:
                prevNode.next = currentNode.next
            else:
                prevNode = prevNode.next
            currentNode = currentNode.next
        return head.next