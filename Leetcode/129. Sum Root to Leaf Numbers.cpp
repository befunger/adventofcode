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
    int sumNumbers(TreeNode* root) {
        // DFS down to leaves. At each iteration change val = 10*val + new_val
        return findSum(root, 0);
    }
    int findSum(TreeNode* node, int current_value){
        // Update value (10*AB + C = ABC)
        current_value = 10*current_value + node->val;
        // Return path-to-leaf number if at a leaf node
        if(!node->left && !node->right) return current_value;
        // Else, return sum of children (if only one child the other will return 0)
        else return (node->left ? findSum(node->left, current_value) : 0) + 
                    (node->right ? findSum(node->right, current_value) : 0);
    }
};