#include <vector>
#include <queue>
using namespace std;

//Definition for a binary tree node. 
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
    int minDepth(TreeNode* root) {
        /*Find minimum depth of binary tree. We use BFS to avoid exploring more nodes than necessary.*/
        if(!root) return 0;

        queue<TreeNode*> nodes;
        nodes.push(root);

        int level_size = 1;
        int depth = 1;

        // Keep going until no elements in the queue
        while(!nodes.empty()){
            // Pop first element and add to level
            TreeNode* node = nodes.front();
            nodes.pop();

            if(!node->left && !node->right){return depth;} // Found first leaf node, return 
            if(node->left) nodes.push(node->left);
            if(node->right) nodes.push(node->right);

            level_size--;
            if(level_size == 0){ // When finished with one level, start next level and increase depth
                level_size = nodes.size();
                depth++;
            }
        }
        return depth; // Should never reach this point
    }
};