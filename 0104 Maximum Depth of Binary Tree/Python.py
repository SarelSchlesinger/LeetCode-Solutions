class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# first approach - iterative DFS algorithm
# time complexity: O(V + E)
# space complexity: O(V)
        
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        stack = [(root, 1)]
        maxDepth = 0
        while stack:
            node, depth = stack.pop()
            maxDepth = max(maxDepth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return maxDepth
        
# second approach - recursive DFS algorithm
# time complexity: O(V + E)
# space complexity: O(V)

class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))