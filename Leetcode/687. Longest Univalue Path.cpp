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
    int longestUnivaluePath(TreeNode* root) {
        // Perform a recursion where each node checks its value + length of both children with that value.
        // If a child has a different value set length to 0
        // In each loop of the recursion update max_length accordingly
        int max_length = 0;
        rec(root, max_length);
        return max_length;
    }

    int rec(TreeNode* node, int &max_length){
        if(!node) return 0;
        // Get longest univalue with one end in children
        int left = rec(node->left, max_length);
        int right = rec(node->right, max_length);
        // Set to 0 if value is different
        if(left && node->left->val != node->val) left = 0;
        if(right && node->right->val != node->val) right = 0;
        // Update max_length if applicable
        max_length = max(max_length, left+right);
        // Return longest univalue path ending in node
        return 1 + max(left, right);

    }
};