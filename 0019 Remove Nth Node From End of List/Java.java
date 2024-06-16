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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ArrayList<ListNode> stack = new ArrayList<>();
        while (head != null) {
            stack.add(head);
            head = head.next;
        }
        if (stack.size() == 1) return null;
        if (n == 1) {
            stack.get(stack.size() - 2).next = null;
        } else if (n == stack.size()) {
            return stack.get(1);
        } else {
            stack.get(stack.size() - n - 1).next = stack.get(stack.size() - n + 1);
        }
        return stack.get(0);
    }
}

// second approach - using two pointers
// time complexity: O(n)
// space complexity: O(1)       
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
       ListNode fast = head, slow = head;
        for (int i = 0; i < n; i++) {
            fast = fast.next;
        }  
        if (fast == null) {
            return head.next;
        }
        while (fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;
        return head;
    }
}