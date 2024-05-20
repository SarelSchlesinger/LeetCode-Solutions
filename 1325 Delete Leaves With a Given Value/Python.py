# time Complexity: O(n)
# space complexity: O(n)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    
    def isLeaf(self, node):
        return not node.left and not node.right
    
    def removeLeafNodes(self, root, target):
        stack = [root]
        i = 0
        while i < len(stack):
            if stack[i].left:
                stack.append(stack[i].left)
            if stack[i].right:
                stack.append(stack[i].right)
            i += 1
        i = len(stack) - 1
        while i >= 0:
            if not self.isLeaf(stack[i]):
                if stack[i].left and self.isLeaf(stack[i].left) and stack[i].left.val == target:
                    stack[i].left = None
                if stack[i].right and self.isLeaf(stack[i].right) and stack[i].right.val == target:
                    stack[i].right = None
            i -= 1
        return None if self.isLeaf(stack[0]) and stack[0].val == target else stack[0]