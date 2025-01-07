// time complexity:  O(n)
// space complexity: O(log(n))

public class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;
	TreeNode() {}
	TreeNode(int val) { this.val = val; }
	TreeNode(int val, TreeNode left, TreeNode right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}
}

class Solution {
    
    public TreeNode sortedArrayToBST(int[] nums) {
        return sortedArrayToBST_helper(nums, 0, nums.length - 1);
    }
    
    public TreeNode sortedArrayToBST_helper(int[] nums, int leftIndex, int rightIndex) {
        if (leftIndex > rightIndex) return null;
        return new TreeNode(nums[(rightIndex + leftIndex) / 2],
                            sortedArrayToBST_helper(nums, leftIndex, (rightIndex + leftIndex) / 2 - 1),
                            sortedArrayToBST_helper(nums, (rightIndex + leftIndex) / 2 + 1, rightIndex));
    }
}