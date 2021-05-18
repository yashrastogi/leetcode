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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        
        ListNode c1 = l1, c2 = l2;
        ListNode head_ret = null, curr_ret = null;
        
        while(c1 != null && c2 != null) {
            int curr_sum = c1.val + c2.val + carry;
            if (curr_sum >= 10) {
                carry = 1;
                curr_sum -= 10;
            } else {
                carry = 0;
            }
            if (curr_ret == null) {
                curr_ret = new ListNode(curr_sum);
                head_ret = curr_ret;
                curr_ret.next = new ListNode();
            } else {
                curr_ret = curr_ret.next;
                curr_ret.val = curr_sum;
                curr_ret.next = new ListNode();
            }
            c1 = c1.next;
            c2 = c2.next;
        }
        
        while(c1 != null) {
            int curr_sum = c1.val + carry;
            if (curr_sum >= 10) {
                carry = 1;
                curr_sum -= 10;
            } else {
                carry = 0;
            }
            if (curr_ret == null) {
                curr_ret = new ListNode(curr_sum);
                head_ret = curr_ret;
                curr_ret.next = new ListNode();
            } else {
                curr_ret = curr_ret.next;
                curr_ret.val = curr_sum;
                curr_ret.next = new ListNode();
            }
            c1 = c1.next;
        }
        
        while(c2 != null) {
            int curr_sum = c2.val + carry;
            if (curr_sum >= 10) {
                carry = 1;
                curr_sum -= 10;
            } else {
                carry = 0;
            }
            if (curr_ret == null) {
                curr_ret = new ListNode(curr_sum);
                head_ret = curr_ret;
                curr_ret.next = new ListNode();
            } else {
                curr_ret = curr_ret.next;
                curr_ret.val = curr_sum;
                curr_ret.next = new ListNode();
            }
            c2 = c2.next;
        }
        
        if(carry == 1) {
            curr_ret = curr_ret.next;
            curr_ret.val = carry;
            curr_ret.next = new ListNode();
        }
        curr_ret.next = null;
        return head_ret;
    }
}