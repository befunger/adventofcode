// Definition for a binary tree node.
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
    bool hasPathSum(TreeNode* root, int targetSum) {
        /*Check if any root-to-leaf path matches target sum. Recursive implementation.*/

        // Empty tree has no paths
        if(!root) return false;
        // Root node, return true for this path if matches
        if(!root->left && !root->right) return root->val == targetSum;
        // Check if potential left node has a path with remaining sum when subtracting this nodes value
        else if(root->left && hasPathSum(root->left, targetSum-root->val)) return true;
        // Same for right node
        else return root->right && hasPathSum(root->right, targetSum-root->val);
    }
};