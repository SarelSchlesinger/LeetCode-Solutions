# time complexity: O(n)
# space complexity: O(n)

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    
    def isValidBST(self, root):
        return self.isValid(root, -pow(2, 31) - 1, pow(2, 31))

    def isValid(self, node, min_val, max_val):
        if not node: return True
        if not (min_val < node.val < max_val): return False
        return self.isValid(node.left, min_val, node.val) and self.isValid(node.right, node.val, max_val)