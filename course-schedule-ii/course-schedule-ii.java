class Solution {
    Map<Integer, List<Integer>> vertices;
    Boolean hasCycle = false;
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        vertices = new HashMap<Integer, List<Integer>>();
        for(var edge: prerequisites) {
            var list = vertices.getOrDefault(edge[0], new ArrayList<Integer>());
            list.add(edge[1]);
            vertices.put(edge[0], list);
        }
        var visited = new HashSet<Integer>();
        var stack = new ArrayDeque<Integer>();
        var visitedCurr = new HashSet<Integer>();
        for(int i=0; i<numCourses; i++) {
            if(!visited.contains(i)) 
                topSort(i, visited, stack, visitedCurr);
        }
        if (hasCycle) {
            print("hasCycle");
            return new int[0];
        }
        else {
            int[] res1 = new int[stack.size()];
            int count = stack.size() - 1;
            for(var a: stack) {
                res1[count] = a;
                count--;
            }
            return res1;
        }
    }
    
    public void topSort(int vertex, Set<Integer> visited, Deque<Integer> stack, Set<Integer> visitedCurr) {
        visited.add(vertex);
        visitedCurr.add(vertex);
        for(var nbr: vertices.getOrDefault(vertex, new ArrayList<Integer>())) {
            if(!visited.contains(nbr)) {
                topSort(nbr, visited, stack, visitedCurr);
            }
            else if(visitedCurr.contains(nbr)) {
                hasCycle = true;   
            }
        }
        visitedCurr.remove(vertex);
        stack.addFirst(vertex);
    }
    
    public static void print(Object o, String sep) {
        System.out.print(o + sep);
    }
    public static void print(Object o) {
        print(o, "\n");
    }
}