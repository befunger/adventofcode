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

    ListNode* reverseKGroup(ListNode* head, int k) {
        /*Reverse every group of size K in the list individually. Any leftover nodes at end remain unchanged*/
        if(k==1){return head;}

        // Create placeholder node before head
        ListNode *pre_head = new ListNode(0);
        pre_head->next = head;


        return pre_head->next;
    }
};