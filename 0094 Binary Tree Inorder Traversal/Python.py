# time complexity:  O(n)
# space complexity: O(n)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        if not root: return None
        if not root.left and not root.right:
            return [root.val]
        if root.left and root.right:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        if root.left:
            return self.inorderTraversal(root.left) + [root.val]
        return [root.val] + self.inorderTraversal(root.right)