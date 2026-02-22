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

// first approach - recursive DFS algorithm
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) return 1;
        if (root.left != null && root.right != null)
            return 1 + Math.min(minDepth(root.left), minDepth(root.right));
        if (root.left != null) return 1 + minDepth(root.left);
        return 1 + minDepth(root.right);
    }
}

// second approach - iterative DFS algorithm
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        Deque<TreeNode> nodes = new ArrayDeque<>();
        Deque<Integer> height = new ArrayDeque<>();
        nodes.addFirst(root);
        height.addFirst(1);
        int minHeight = Integer.MAX_VALUE;
        while (!nodes.isEmpty()) {
            TreeNode currentNode = nodes.removeFirst();
            int currentHeight = height.removeFirst();
            if (currentNode.left == null && currentNode.right == null) minHeight = Math.min(currentHeight, minHeight);
            else {
                if (currentNode.right != null) {
                    nodes.addFirst(currentNode.right);
                    height.addFirst(currentHeight + 1);
                }
                if (currentNode.left != null) {
                    nodes.addFirst(currentNode.left);
                    height.addFirst(currentHeight + 1);
                }
            }
        }
        return minHeight;
    }
}