using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* old_head = head;

        // Count number of nodes
        int n = 0;
        while(head){
            n++;
            head=head->next;
        }

        k = k>n/2 ? n-k+1 : k; // If k > n/2 we swap it for the equivalent smaller k
        
        head = old_head; // Reset head for second sweep
        
        for(int i = 1; i<k; i++){head=head->next;}
        ListNode* first = head; // k:th node
        for(int i = k; i<=n-k; i++){head=head->next;}
        ListNode* second = head; // (n-k):th node

        swap(first->val, second->val);

        return old_head;
    }
};