using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    void reverseNextK(ListNode* &node, int K){
        /*Given a node, reverses the proceeding K nodes in that list.*/
        
        // If there are less than K nodes proceeding, do nothing
        ListNode* temp = node;
        for(int i=0; i < K; i++){
            temp = temp->next;
            if(!temp){return;}
        }

        ListNode *prev = node;
        ListNode *curr = prev->next;
        ListNode *after;
        for(int i = 1; i < K; i++){
            after = prev->next;
            prev->next = curr->next;
            curr->next = curr->next->next;
            prev->next->next = after;
        }
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        /*Reverse every group of size K in the list individually. Leftover nodes at end remain unchanged*/
        if(k==1){return head;}

        // NOTE: This apparently causes a memory leak as new keyword stores variable on the heap (dynamic) and does not clean up
        // ListNode *pre_head = new ListNode(0);
        // pre_head->next = head;

        // Create placeholder node before head (on heap)
        ListNode pre_head(0, head);

        int i = 0;
        ListNode *node = &pre_head;
        while(node){
            if(i%k == 0){ // Flip at every k:th node
                reverseNextK(node, k);
            }
            node = node->next;
            i++;
        }

        return pre_head.next;
    }
};