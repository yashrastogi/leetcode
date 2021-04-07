/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        var firstNodeCopy = recurse(node, new HashMap<Integer, Node>());
        return firstNodeCopy;
    }
    
    public Node recurse(Node node, Map<Integer, Node> dupNodes) {
        if(node == null) {
            return null;
        }
        dupNodes.put(node.val, new Node(node.val));
        var neighbors = new ArrayList<Node>();
        for(var neighbor: node.neighbors) {
            if(dupNodes.containsKey(neighbor.val)) {
                neighbors.add(dupNodes.get(neighbor.val));
            } else {
                neighbors.add(recurse(neighbor, dupNodes));    
            }
        }
        var temp = dupNodes.get(node.val);
        temp.neighbors = neighbors;
        dupNodes.put(node.val, temp);
        return temp;
    }
    
    public void print(Object o, String sep) {
        System.out.print(o + sep);
    }
    public void print(Object o) {
        print(o, "\n");
    }
    public void printN(Node n) {
        print(n.val, " n: ");
        for (var a: n.neighbors) {
            print(a.val, " ");
        }
        print("");
    }
}