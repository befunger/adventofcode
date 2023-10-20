/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode curr = head;
        int numNodes = 1;
        while(curr.next != null){
            numNodes++;
            curr = curr.next;
        }
        numNodes = numNodes/2;
        while(numNodes > 0){
            head = head.next;
            numNodes--;
        }
        return head;
    }
}