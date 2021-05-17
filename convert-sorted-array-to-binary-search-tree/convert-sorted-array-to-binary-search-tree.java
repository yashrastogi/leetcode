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
    public TreeNode sortedArrayToBST(int[] nums) {
        return generateBST(0, nums.length-1, nums);
    }
    
    public TreeNode generateBST(int lo, int hi, int[] nums) {
        if (lo > hi) {
            return null;
        }
        int mid = (lo + hi) / 2;
        var node = new TreeNode(nums[mid]);
        node.left = generateBST(lo, mid-1, nums);
        node.right = generateBST(mid+1, hi, nums);
        return node;
    }
}