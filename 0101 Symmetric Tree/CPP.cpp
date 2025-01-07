// time complexity:  O(n)
// space complexity: balanced tree case   --> O(log(n))
//                   unbalanced tree case --> O(n)

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
    
	bool isSymmetric(TreeNode* root) {
        return isSymmetricHelper(root->left, root->right);
    }

    bool isSymmetricHelper(TreeNode* leftNode, TreeNode* rightNode) {
        if (leftNode == nullptr && rightNode == nullptr) return true;
        if (leftNode == nullptr || rightNode == nullptr) return false;
        return leftNode->val == rightNode->val
				&& isSymmetricHelper(leftNode->left, rightNode->right)
				&& isSymmetricHelper(leftNode->right, rightNode->left);
    }
};