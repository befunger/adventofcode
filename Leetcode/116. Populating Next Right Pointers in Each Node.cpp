using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;
    Node() : val(0), left(nullptr), right(nullptr), next(nullptr) {}
    Node(int _val) : val(_val), left(nullptr), right(nullptr), next(nullptr) {}
    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};

class Solution {
public:
    Node* connect(Node* root) {
        /*Given a perfect binary tree, give each node a next pointer to the next node on the same layer
         If there is no next node, leave as NULL*/
        if(!root || !root->left) return root; // If node is null or has no children, do nothing
        root->left->next = root->right; // Left child points at right child
        if(root->next) root->right->next = root->next->left; // Right node points at (possible) left child of next node
        connect(root->left);
        connect(root->right);
        return root;
    }
};