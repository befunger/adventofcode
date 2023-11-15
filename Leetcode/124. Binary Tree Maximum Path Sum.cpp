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
    int maxPathSum(TreeNode* root) {
        // Default case with root value (always at least 1 node)
        int sum = root->val;
        // Begin recursion with root 
        pathSum(root, sum);
        return sum;
    }
    int pathSum(TreeNode* root, int &sum) {
        // Return 0 for non-existent nodes
        if(!root) return 0;
        // Get max path sum with end in children
        int left = pathSum(root->left, sum);
        int right = pathSum(root->right, sum);
        int best = max(left, right);

        //Replace sum if a better option is found
        sum = max(sum, root->val+left+right); // Path going down left and right
        sum = max(sum, root->val+best);       // Path using one tail (better if one has negative sum)
        sum = max(sum, root->val);            // This node only (better if both have negative sum)

        // Return max path sum with one end at this node (use best tail or neither if both negative)
        return root->val + max(best, 0);
    }
};