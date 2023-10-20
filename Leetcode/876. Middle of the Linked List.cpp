
 // Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        /* Return the middle node of a linked list (if two middle nodes, return the second)*/

        ListNode *slow_ptr = head;

        while(head != nullptr && head->next != nullptr){
            head = head->next->next;
            slow_ptr = slow_ptr->next;            
        }

        return slow_ptr;
    }
};