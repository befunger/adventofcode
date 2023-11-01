using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        /*Take the k last nodes from the list and move them to the start*/

        // Rotation does nothing to empty/single element list
        if(head == nullptr || head->next == nullptr){return head;}

        // Count number of nodes
        int n = 1;
        ListNode* node = head;
        while(node->next){
            n++;
            node=node->next;
        }

        // Connect end to start (now a cycle)
        node->next = head;

        // Iterate until new end and disconnect
        int start_index = n-(k%n)+1;
        for(int i = 1; i < start_index; i++){
            node=node->next;
        }
        head = node->next; // Save new head
        node->next = nullptr; // Disconnect end from head
        return head;
    }
};