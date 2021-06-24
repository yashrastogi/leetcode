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
    public List<Integer> inorderTraversal(TreeNode root) {
        var ret = new ArrayList<Integer>();
        dfs(root, ret);
        return ret;
    }
    
    private void dfs(TreeNode node, List<Integer> list) {
        if(node == null) return;
        dfs(node.left, list);
        list.add(node.val);
        dfs(node.right, list);
    }
}