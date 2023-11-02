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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        /*Identical to 102, except reverse the vector. 
          Why make it more fancy when easy does it with no added time/space complexity?*/

        vector<vector<int>> level_order_traversal;
        if(!root){return level_order_traversal;}

        queue<TreeNode*> nodes;
        nodes.push(root);
        vector<int> level; 
        int level_size = 1; // Number of elements left in the current level

        // Keep going until no elements in the queue
        while(!nodes.empty()){
            // Pop first element and add to level
            TreeNode* node = nodes.front();
            nodes.pop();
            level.push_back(node->val);

            // Add potential children to queue
            if(node->left){
                nodes.push(node->left);
            }
            if(node->right){
                nodes.push(node->right);
            }

            level_size--;
            if(level_size == 0){ // When finished with one level, start next level and reset size
                level_order_traversal.push_back(level);
                level_size = nodes.size(); // All remaining are next level
                level = vector<int>();
            }
        }

        reverse(level_order_traversal.begin(),level_order_traversal.end());
        return level_order_traversal;
    }
};