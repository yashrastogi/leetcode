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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode c1=null, c2=head;
        int count = 0;
        while(c2 != null) {
            if (c1 != null) {
                c1 = c1.next;
            }
            if(count == n) {
                c1 = head;
            }
            c2 = c2.next;
            count++;
        }
        
        if (c1 == null) { // remove first node
            head = head.next;
        } else if(c1.next != null) { // middle node
            c1.next = c1.next.next;    
        } 
        
        
        
        
        return head;
    }
}