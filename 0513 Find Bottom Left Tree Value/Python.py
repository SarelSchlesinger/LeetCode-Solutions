# using BFS algorithm
# Time complexity: O(V + E)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def findBottomLeftValue(self, root):
        queue = [(root, 1)]
        lastRow = 1
        res = root
        while queue:
            node, row = queue.pop(0)
            if row > lastRow:
                res = node
                lastRow += 1
            if node.left:
                queue.append((node.left, row + 1))
            if node.right:
                queue.append((node.right, row + 1))
        return res.val