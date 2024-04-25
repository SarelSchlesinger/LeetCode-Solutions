# using DFS

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def leafSimilar(self, root1, root2):
        
        def findAllLeaves(root):
            stack = [root]
            leaves = list()
            while stack:
                node = stack.pop()
                if not node.left and not node.right:
                    leaves.append(node.val)
                else:
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
            return leaves

        return findAllLeaves(root1) == findAllLeaves(root2)