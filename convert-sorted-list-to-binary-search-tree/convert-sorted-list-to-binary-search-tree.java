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
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if(head == null) return null;
        ListNode mid = head, midPrev = null, fast = head;
        for(fast = head; fast != null && fast.next != null; fast = fast.next.next) {
            midPrev = mid;
            mid = mid.next;
        }
        if(mid == head) return new TreeNode(head.val);
        midPrev.next = null;
        if(mid.next != null)
            return new TreeNode(mid.val, sortedListToBST(head), sortedListToBST(mid.next));
        else
            return new TreeNode(mid.val, sortedListToBST(head), null);
    }
    
    void printList(ListNode a) {
        for(; a != null; a = a.next) p.accept(a.val + " ");
        p.accept("\n");
    }
    
    Consumer<Object> p;
    public Solution() {
        p = o -> System.out.print(o);
    }
}