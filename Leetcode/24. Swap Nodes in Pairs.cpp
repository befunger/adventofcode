using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        /*Swap all pairs of nodes*/
        ListNode* pre_head = new ListNode(0); // Dummy node to point at head since head might swap
        pre_head->next = head;

        ListNode *node = pre_head;
        while(node->next && node->next->next){ // Change 0->1->2->3 to 0->2->1->3 (3 might be null)
            ListNode *temp = node->next->next; // Save 2
            node->next->next = temp->next; // 1 points to 3
            temp->next = node->next; // 2 points to 1
            node->next = temp; // 0 points to 2
            node = node->next->next; // Iterate forwards 2 steps
        }
        return pre_head->next;
    }
};