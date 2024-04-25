# using BFS algorithm
# Time complexity: O(V + E)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root):
        res = 0
        queue = [(root, 'R')]
        while queue:
            node, side = queue.pop(0)
            if not node.left and not node.right:
                if side == 'L':
                    res += node.val
            else:
                if node.left:
                    queue.append((node.left, 'L'))
                if node.right:
                    queue.append((node.right, 'R'))
        return res