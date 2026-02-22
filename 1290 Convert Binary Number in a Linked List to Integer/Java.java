public class ListNode {
	int val;
	ListNode next;
	ListNode() {}
	ListNode(int val) { this.val = val; }
	ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

// time complexity:  O(n)
// space complexity: O(n)

class Solution {
    public int getDecimalValue(ListNode head) {
        Deque<Integer> stack = new ArrayDeque<>();
        while (head != null) {
            stack.add(head.val);
            head = head.next;
        }
        int p = 1, num = 0;
        while (!stack.isEmpty()) {
            if (stack.removeLast() == 1) num += p;
            p *= 2;
        }
        return num;
    }
}