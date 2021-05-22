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
    public List<List<Integer>> levelOrder(TreeNode root) {
        var ret = new ArrayList<List<Integer>>();
        if(root == null) return ret;
        var q = new ArrayDeque<TreeNode>();
        q.add(root);
        var map = new HashMap<TreeNode, Integer>();
        map.put(root, 0);
        ret.add(Arrays.asList(root.val));
        while(q.size() != 0) {
            var cur = q.poll();
            while(ret.size()-1 < map.get(cur)+1) {
                ret.add(new ArrayList<Integer>());
            }
            if(cur.left != null) {
                q.add(cur.left);
                ret.get(map.get(cur)+1).add(cur.left.val);
                map.put(cur.left, map.get(cur)+1);
            }
            if(cur.right != null) {
                q.add(cur.right);
                ret.get(map.get(cur)+1).add(cur.right.val);
                map.put(cur.right, map.get(cur)+1);
            }
        }
        if(ret.get(ret.size()-1).size() == 0) {
            ret.remove(ret.size()-1);
        } 
        return ret;
    }
}