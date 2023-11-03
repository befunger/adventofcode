#include <vector>
#include <queue>
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
    vector<int> rightSideView(TreeNode* root) {
        /*Return a vector of all "visible" nodes from the right of the binary tree
        This amounts to returning the rightmost node on every level of the tree
        
        If we iterate right-to-left we can return the first node we find on each level*/
        vector<int> rightmost_nodes;
        if(!root) return rightmost_nodes;

        queue<TreeNode*> nodes;
        nodes.push(root);
        vector<int> level; 
        int level_size = 1;
        int depth = 1;

        while(!nodes.empty()){
            // Grab first node (right-to-left)
            TreeNode* node = nodes.front();
            nodes.pop();

            // Add rightmost from each depth to output
            if(rightmost_nodes.size() < depth) rightmost_nodes.push_back(node->val);

            // Add potential children right-to-left
            if(node->right) nodes.push(node->right);
            if(node->left) nodes.push(node->left);

            // Increase depth when all on this level have been handled
            level_size--; 
            if(level_size == 0){
                level_size = nodes.size();
                depth++;
            }
        }
        return rightmost_nodes;
    }
};