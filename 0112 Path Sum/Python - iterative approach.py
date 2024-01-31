class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None: return False
        stack = [(root, root.val)]
        while stack:
            currentNode, currentVal = stack.pop()
            if not currentNode.left and not currentNode.right and targetSum == currentVal:
                return True
            if currentNode.left:
                stack.append((currentNode.left, currentVal + currentNode.left.val))
            if currentNode.right:
                stack.append((currentNode.right, currentVal + currentNode.right.val))
        return False