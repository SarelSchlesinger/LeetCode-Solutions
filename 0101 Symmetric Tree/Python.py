# time complexity:  O(n)
# space complexity: balanced tree case   --> O(log(n))
#                   unbalanced tree case --> O(n)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    
    def isSymmetric(self, root):
        
        def helper(leftNode, rightNode):
            if not leftNode and not rightNode: return True
            if not leftNode or not rightNode: return False
            return leftNode.val == rightNode.val and helper(leftNode.left, rightNode.right) and helper(leftNode.right, rightNode.left)
        
        return helper(root.left, root.right)
        