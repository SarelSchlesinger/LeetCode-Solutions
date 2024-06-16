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

// first approach - iterative DFS algorithm
// time complexity: O(V + E)
// space complexity: O(V)

class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        int maxDepth = 0;
        ArrayList<TreeNode> stackNodes = new ArrayList<>();
        ArrayList<Integer> stackDepth = new ArrayList<>();
        stackNodes.add(root);
        stackDepth.add(1);
        while (!stackNodes.isEmpty()) {
            TreeNode currentNode = stackNodes.remove(stackNodes.size() - 1);
            int currentDepth = stackDepth.remove(stackDepth.size() - 1);
            maxDepth = Math.max(maxDepth, currentDepth);
            if (currentNode.left != null) {
                stackNodes.add(currentNode.left);
                stackDepth.add(currentDepth + 1);
            }
            if (currentNode.right != null) {
                stackNodes.add(currentNode.right);
                stackDepth.add(currentDepth + 1);
            }
        }
        return maxDepth;
    }
}
// second approach - recursive DFS algorithm
// time complexity: O(V + E)
// space complexity: O(V)

class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}