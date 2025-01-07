// time complexity:  O(n)
// space complexity: O(n)

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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        if (root == nullptr) {
            return res;
        }
        if (root->left != nullptr) {
            res = inorderTraversal(root->left);            
        } 
        res.push_back(root->val);
        if (root->right != nullptr) {
            vector<int> sub_tree = inorderTraversal(root->right);
            res.insert(res.end(), sub_tree.begin(), sub_tree.end());
        } 
        return res;
    }
};