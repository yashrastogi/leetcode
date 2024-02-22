class Solution {
  int minReorder(int n, List<List<int>> connections) {
    final visited = Set<int>();

    int dfs(int curr, Map<int, List<List<int>>> graph) {
      visited.add(curr);
      var changeCount = 0;
      for (final city in graph[curr]!) {
        if (!visited.contains(city[0])) {
          changeCount += dfs(city[0], graph) + city[1];
        }
      }
      return changeCount;
    }

    final graph = <int, List<List<int>>>{};
    for (final connection in connections) {
      final i = connection[0];
      final j = connection[1];
      if (!graph.containsKey(j)) graph[j] = [];
      graph[j]!.add([i, 0]); // reverse edge
      if (!graph.containsKey(i)) graph[i] = [];
      graph[i]!.add([j, 1]); // forward edge
    }

    return dfs(0, graph);
  }
}
