#include <vector>
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
    int paths = 0;
    int pathSum(TreeNode* root, int targetSum) {
        // Empty node has no paths
        if(!root) return 0;

        // Check if this node has path
        findPath(root, targetSum);
        // Check children (will return 0 if nullptr)
        pathSum(root->left, targetSum);
        pathSum(root->right, targetSum);

        return paths;
    }
    void findPath(TreeNode* node, long currentSum){
        // Update current sum
        currentSum -= node->val;

        // If this node matches target sum, increment num of paths
        if(!currentSum) paths++;

        // Call child nodes with updated currentSum
        if(node->left) findPath(node->left, currentSum);
        if(node->right) findPath(node->right, currentSum);
    }
};