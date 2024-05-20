// time complexity: O(1)
// space complexity: O(1)
 
 public class ListNode {
	 int val;
	 ListNode next;
	 ListNode(int x) { val = x; }
}
 
class Solution {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}