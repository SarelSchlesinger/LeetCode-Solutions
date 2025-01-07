// time complexity:  O(n)
// space complexity: O(log(n))

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return sortedArrayToBST_helper(nums, 0, nums.size() - 1);
    }
    
    TreeNode* sortedArrayToBST_helper(vector<int>& nums, int leftIndex, int rightIndex) {
        if (leftIndex > rightIndex) return nullptr;
        return new TreeNode(nums[(rightIndex + leftIndex) / 2],
                            sortedArrayToBST_helper(nums, leftIndex, (rightIndex + leftIndex) / 2 - 1),
                            sortedArrayToBST_helper(nums, (rightIndex + leftIndex) / 2 + 1, rightIndex));
    }
};