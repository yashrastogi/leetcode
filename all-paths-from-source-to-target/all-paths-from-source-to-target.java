class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        int count = 0;
        for (var path: graph) {
            print("Node " + count + " is connected to", " ");
            for(var ver: path) {
                print(ver, ", ");
            }
            print("");
            count++;
        }
        var paths = new ArrayList<List<Integer>>();
        recurse(graph, new ArrayList<Integer>(Arrays.asList(0)), paths);
        return paths;
    }
    
    public void recurse(int[][] graph, List<Integer> path, List<List<Integer>> paths) {
        var adjMx = graph[path.get(path.size()-1)];
        for (var el: adjMx) {
            var pathDup = new ArrayList<Integer>(path);
            pathDup.add(el);    
            if (el == graph.length-1) {
                paths.add(pathDup);
            } else {
                recurse(graph, pathDup, paths);
            }
        }
    }
    
    public void print(Object o, String sep) {
        System.out.print(o + sep);
    }
    public void print(Object o) {
        print(o, "\n");
    }
}