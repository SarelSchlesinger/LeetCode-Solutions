// time complexity: O(n)
// space complexity: O(1)

public class ListNode {
	int val;
	ListNode next;
	ListNode() {}
	ListNode(int val) { this.val = val; }
	ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {

    public ListNode reversedLinkedList(ListNode head) {
        ListNode prevNode = null;
        ListNode nextNode = null;
        while (head != null) {
            nextNode = head.next;
            head.next = prevNode;
            prevNode = head;
            head = nextNode;
        }
        return prevNode;
    }

    public boolean isPalindrome(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode tail = reversedLinkedList(slow);
        while (tail != null) {
            if (tail.val != head.val) return false;
            tail = tail.next;
            head = head.next;
        }
        return true;
    }
}