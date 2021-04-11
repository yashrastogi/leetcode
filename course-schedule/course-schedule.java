class Solution {
    Map<Integer, List<Integer>> vertices;
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        vertices = new HashMap<Integer, List<Integer>>();
        for (var edge: prerequisites) {
            var list = vertices.getOrDefault(edge[0], new ArrayList<Integer>());
            list.add(edge[1]);
            vertices.put(edge[0], list);
        }
        var visited = new HashSet<Integer>();
        var stack = new Stack<Integer>();
        for (int i=0; i<numCourses; i++) {
            if (!visited.contains(i)) {
                if(hasCycle(i, visited, stack)) return false;
            }
        }
        return true;
    }
    
    public boolean hasCycle(int vertex, Set<Integer> visited, Stack<Integer> stack, Set<Integer> visitedCurr) {
        visited.add(vertex);
        visitedCurr.add(vertex);
        for(var nbr: vertices.getOrDefault(vertex, new ArrayList<Integer>())) {
            if (!visited.contains(nbr)) {
                if (hasCycle(nbr, visited, stack, visitedCurr)) return true;
            }
            else if (visitedCurr.contains(nbr)) {
                return true;
            }
        }
        visitedCurr.remove(vertex);
        stack.push(vertex);
        return false;
    }
    
    public boolean hasCycle(int vertex, Set<Integer> visited, Stack<Integer> stack) {
        return hasCycle(vertex, visited, stack, new HashSet<Integer>());
    }
    
    public static void print(Object o, String sep) {
        System.out.print(o + sep);
    }
    public static void print(Object o) {
        print(o, "\n");
    }
}