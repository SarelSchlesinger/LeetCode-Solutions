public class ListNode {
	int val;
	ListNode next;
	ListNode() {}
	ListNode(int val) { this.val = val; }
	ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
 
// first approach - using stack
// time complexity: O(n)
// space complexity: O(n)
class Solution {
    public ListNode reverseList(ListNode head) {
        ArrayList<ListNode> stack = new ArrayList<>();
        if (head == null) return null;
        while (head != null) {
            stack.add(head);
            head = head.next;
        }
        for (int i = stack.size() - 1; i > 0; i--) {
            stack.get(i).next = stack.get(i - 1);
        }
        stack.get(0).next = null;
        return stack.get(stack.size() - 1);
    }
}

// second approach - using two pointers
// time complexity: O(n)
// space complexity: O(1)
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prevNode = null, nextNode = null;
        while (head != null) {
            nextNode = head.next;
            head.next = prevNode;
            prevNode = head;
            head = nextNode;
        }
        return prevNode;
    }
}