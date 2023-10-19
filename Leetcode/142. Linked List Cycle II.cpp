# include <iostream>
# include <unordered_set>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        /*Given the root of a linked list, return the starting node of a potential loop (or null if no loop).
        The starting node of the loop is the loop which the final node points back at.*/

        /*O(1) space solution based on slow/fast ptr*/
        

        /*Hashmap solution, needs O(n) space*/
        unordered_set<ListNode *> nodes;
        int iters = 0;
        while(head != nullptr){
            int old_size = nodes.size();
            nodes.insert(head);
            if(nodes.size() == old_size){ // The first detected duplicate is the one where the cycle "starts"
                return head; 
            }
            head = head->next;
            iters++;
        }
        return head; // If we reach the end, return the nullptr
    }
};