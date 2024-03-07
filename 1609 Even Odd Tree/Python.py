# using BFS algorithm
# Time complexity: O(V + E)

class Solution(object):
    def isEvenOddTree(self, root):
        queue = [(root, 0)]
        currentRow = None
        val = None
        while queue:
            node, row = queue.pop(0)
            if (row % 2 == 0 and node.val % 2 == 0) or (row % 2 == 1 and node.val % 2 == 1):
                return False
            if val is None:
                currentRow = 0
                val = node.val
            elif row > currentRow:
                currentRow += 1
                val = node.val
            elif (row % 2 == 0 and node.val > val) or (row % 2 == 1 and node.val < val):
                val = node.val
            else:
                return False
            if node.left:
                queue.append((node.left, row + 1))
            if node.right:
                queue.append((node.right, row + 1))
        return True