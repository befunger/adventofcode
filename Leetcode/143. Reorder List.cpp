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
    void reorderList(ListNode* head) {
        /*Reorder the nodes of a linked list by zipper-merging the first half with the second half reversed
        Before:     a -> b -> c -> d -> e -> f
        After:      a -> f -> b -> e -> c -> d
        */

        /*O(n) time, O(1) space by in-place reversing second half of the list and merging*/
        ListNode *fast_ptr = head;
        ListNode *slow_ptr = head;
        // Find middle of list
        while(fast_ptr != nullptr && fast_ptr->next != nullptr){
            fast_ptr = fast_ptr->next->next;
            slow_ptr = slow_ptr->next;            
        }
        // Reverse second half in-place
        ListNode *prev = nullptr;
        ListNode *curr = slow_ptr;
        ListNode *after;
        while(curr != nullptr){
            after = curr->next;
            curr->next = prev;
            prev = curr;
            curr = after;
        }
        ListNode *reverse_head = prev;

        // Merge two lists together 
        ListNode *curr_head = head;
        ListNode *front_tail;
        ListNode *back_tail;
        while(reverse_head->next != nullptr){
            front_tail = curr_head->next;
            back_tail = reverse_head->next;
            curr_head->next = reverse_head;
            curr_head->next->next = front_tail;
            curr_head = curr_head->next->next;
            reverse_head = back_tail;
        }
    }
};