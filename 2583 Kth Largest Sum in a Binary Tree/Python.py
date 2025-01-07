# time complexity:  O(n*log(n))
# space complexity: O(n)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        queue = deque([[root, 1]])
        level_sum_list = []
        level_sum = 0
        level = 1
        while len(queue) > 0:
            node, current_level = queue.popleft()
            if current_level > level:
                level_sum_list.append(level_sum)
                level_sum = node.val
                level += 1
            else:
                level_sum += node.val
            if node.left is not None:
                queue.append([node.left, level + 1])
            if node.right is not None:
                queue.append([node.right, level + 1])
        level_sum_list.append(level_sum)
        return -1 if k > level else sorted(level_sum_list)[-k]