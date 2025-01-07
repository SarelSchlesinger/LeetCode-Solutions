# time complexity:  O(n)
# space complexity: O(n)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        res = []
        if not root: return res
        queue = deque([(root, 1)])
        while queue:
            currentNode, level = queue.popleft()
            if level > len(res):
                res.append([])
            res[-1].append(currentNode.val)
            if currentNode.left:
                queue.append((currentNode.left, level + 1))
            if currentNode.right:
                queue.append((currentNode.right, level + 1))
        return res