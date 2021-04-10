class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] seen = new int[numCourses];
        Map<Integer, List<Integer>> graph = new HashMap<>();
        
        for(int[]edge: prerequisites){
            
            if(!graph.containsKey(edge[1])){
                graph.put(edge[1], new LinkedList<>());
            }
            
            graph.get(edge[1]).add(edge[0]);
        }
        
        for(int i = 0; i < numCourses; i++){
            if(!dfs(i, seen, graph)) return false;
        }
        return true;
    }
    
    public boolean dfs(int index, int[] seen, Map<Integer, List<Integer>> graph){
        if(!graph.containsKey(index)){
            seen[index] = 2;
            return true;
        }
        
        seen[index] = 1;
        for(int i: graph.get(index)){
            if(seen[i] == 1) return false;
            if(seen[i] == 0){
                if(!dfs(i, seen, graph)) return false;
            }
        }
        
        seen[index] = 2;
        return true;
    }
}