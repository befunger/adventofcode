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
    std::vector<std::vector<int>> pathSum(TreeNode* root, int targetSum) {
        // Return a list of all root-to-leaf paths that sum to targetSum
        std::vector<std::vector<int>> all_paths;
        // Empty tree has no paths
        if(!root) return all_paths;

        std::vector<int> current_path;
        findPath(root, targetSum, all_paths, current_path);
        return all_paths;
    }
    void findPath(TreeNode* &node, int targetSum, std::vector<std::vector<int>> &all_paths, std::vector<int> current_path){
        // Add the current node to current_path, and remove from target sum
        current_path.push_back(node->val);
        targetSum -= node->val;

        // If this is a leaf node and it matches target sum, add its path
        if(!node->left && !node->right && !targetSum){
            all_paths.push_back(current_path);
        }
        if(node->left) findPath(node->left, targetSum, all_paths, current_path);
        if(node->right) findPath(node->right, targetSum, all_paths, current_path);
    }
};