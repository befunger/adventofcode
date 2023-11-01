using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    void reverseNextGroupIfEven(ListNode* &node, int K){
        /*Given a node, reverses the next UP TO K elements existing, if that number is even.*/
        ListNode* temp = node;
        int k = 0;
        while(temp->next != nullptr && k < K){
            temp = temp->next;
            k++;
        }
        
        if(k%2){ return; } // Group has odd number of elements

        ListNode *prev = node;
        ListNode *curr = prev->next;
        ListNode *after;
        for(int i = 1; i < k; i++){
            after = prev->next;
            prev->next = curr->next;
            curr->next = curr->next->next;
            prev->next->next = after;
        }
    }

    ListNode* reverseEvenLengthGroups(ListNode* head) {
        /*Linked list is split into groups as follows:
        First group is 1 node. Next group is proceeding 2 nodes. Next is proceeding 3 nodes, and so on.
        Note that the last group can have an arbitrarily small number of nodes.
        Reverse every even group in the linked list.*/

        int i = 1;
        int n = 1;
        ListNode *node = head;
        while(node){
            if(i%n == 0){ // We are on the final index of a group, increase number and reset.
                n++;
                i=0;
                // Reverse the next group if it has even number of entries
                reverseNextGroupIfEven(node, n); // Reverses next n entries (if less than n left, do all)

            }
            node = node->next;
            i++;
        }

        return head;
    }
};