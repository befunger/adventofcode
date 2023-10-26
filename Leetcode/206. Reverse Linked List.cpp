using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *prevHead = nullptr; // First node has nullptr as new tail
        ListNode *nextHead;
        while(head){ // Stop when head becomes nullptr
            nextHead = head->next;
            head->next = prevHead;
            prevHead = head;
            head = nextHead;
        }
        return prevHead;
    }
};