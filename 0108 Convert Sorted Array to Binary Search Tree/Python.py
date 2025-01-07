# time complexity:  O(n)
# space complexity: O(log(n))

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    
    def sortedArrayToBST(self, nums):

        def sortedArrayToBST_helper(leftIndex, rightIndex):
            if leftIndex > rightIndex: return None
            return TreeNode(
                nums[(rightIndex + leftIndex) // 2],
                sortedArrayToBST_helper(leftIndex, (rightIndex + leftIndex) // 2 - 1),
                sortedArrayToBST_helper((rightIndex + leftIndex) // 2 + 1, rightIndex))
        
        return sortedArrayToBST_helper(0, len(nums) - 1)