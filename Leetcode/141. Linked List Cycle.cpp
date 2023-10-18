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
    bool hasCycle(ListNode *head) {
        /*Low memory approach with fast and slow pointer*/
        ListNode *fast_ptr = head;
        ListNode *slow_ptr = head;
        while(fast_ptr != nullptr && fast_ptr->next != nullptr){ // If fast pointer reaches null, there's no loop 
            fast_ptr = fast_ptr->next->next;
            slow_ptr = slow_ptr->next;
            if(fast_ptr == slow_ptr){ // If pointers match, there must be a loop (fast "caught up" to slow)
                return true;
            }
        }
        return false;

        /*Hashing approach with O(n) memory and O(n) runtime*/
        unordered_set<ListNode *> nodes;
        int iters = 0;
        while(head != nullptr){
            int old_size = nodes.size();
            nodes.insert(head);
            if(nodes.size() == old_size){ // If adding a node didn't change the size, we have looped and hit a duplicate
                return true;
            }
            head = head->next;
            iters++;
        }
        return false; // If more than 10000 iterations, must be in a loop

    }
};