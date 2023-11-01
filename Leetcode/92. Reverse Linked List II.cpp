using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    void reverseNextK(ListNode* &node, int K){
        /*Given a node, reverses the proceeding K nodes in that list*/
        ListNode *prev = node;
        ListNode *curr = prev->next;
        ListNode *after;
        for(int i = 0; i < K; i++){
            after = prev->next;
            prev->next = curr->next;
            curr->next = curr->next->next;
            prev->next->next = after;
        }
    }
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        /*Reverse part of linked list with indices [left, right]*/
        if(left == right){return head;}

        // Create placeholder node before head
        ListNode *pre_head = new ListNode(0);
        pre_head->next = head;

        // Iterate to node before first to swap (placeholder if left = 1)
        ListNode* prev = pre_head;
        for(int i = 1; i<left; i++){
            prev = prev->next;
        }

        // Reverse next right-left nodes
        reverseNextK(prev, right-left);

        // Return first node in real list (might have changed if swap interval includes first)
        return pre_head->next;
    }
};