#include <algorithm>
using namespace std;
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
    int diameterOfBinaryTree(TreeNode* root) {
        int diameter = 0;
        // Begin recursion with root
        getLongestSubPath(root, diameter);
        return diameter;
    }
    int getLongestSubPath(TreeNode* root, int &diameter) {
        // Return 0 for non-existent nodes
        if(!root) return 0;
        // Get depth of both children
        int left = getLongestSubPath(root->left, diameter);
        int right = getLongestSubPath(root->right, diameter);
        //Replace if this node has higher diameter
        diameter = max(diameter, left+right);
        // Return max depth from this node for previous recursion
        return 1 + max(left, right);
    }
};