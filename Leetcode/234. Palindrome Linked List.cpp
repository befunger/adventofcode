#include <iostream>
#include <vector>
using namespace std;
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
    bool isPalindrome(ListNode* head) {
        /*Check if linked list is palindromic (entries mirror across the middle)*/

        /*O(n) time, O(n) space using stack of first half values*/
        ListNode *fast_ptr = head;
        ListNode *slow_ptr = head;
        vector<int> stack;
        bool move_slow = true;
        while(fast_ptr != nullptr){ // Iterate until slow_ptr is at middle of list
            fast_ptr = fast_ptr->next;
            if(move_slow){
                stack.push_back(slow_ptr->val);
                slow_ptr = slow_ptr->next;
            }
            move_slow = !move_slow;
        }
        if(!move_slow){ // Odd length of linked list, ignore middle element.
            stack.pop_back();
        }

        for(int i = stack.size()-1; i >= 0; i--){ // Compare elements on opposing sides of middle
            if(stack[i] != slow_ptr->val){
                return false;
            }
            slow_ptr = slow_ptr->next;
        }
        return true;
    }
};