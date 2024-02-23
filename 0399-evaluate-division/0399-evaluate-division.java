import java.util.*;

class Solution {
    Map<String, List<Pair>> graph;

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        graph = new HashMap<>();
        for (int i = 0; i < equations.size(); i++) {
            List<String> eq = equations.get(i);
            String src = eq.get(0);
            String dest = eq.get(1);
            double value = values[i];
            graph.putIfAbsent(src, new ArrayList<>());
            graph.putIfAbsent(dest, new ArrayList<>());
            graph.get(src).add(new Pair(dest, value));
            graph.get(dest).add(new Pair(src, 1.0 / value));
        }

        double[] result = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            List<String> query = queries.get(i);
            String src = query.get(0);
            String dest = query.get(1);
            if (!graph.containsKey(src) || !graph.containsKey(dest)) {
                result[i] = -1.0;
            } else {
                result[i] = dfs(src, dest, new HashSet<>());
            }
        }
        return result;
    }

    private double dfs(String curr, String dest, Set<String> visited) {
        visited.add(curr);
        if (curr.equals(dest)) {
            return 1.0;
        }
        double ret_val = -1.0;
        for (Pair neighbor : graph.get(curr)) {
            if (!visited.contains(neighbor.node)) {
                double test = dfs(neighbor.node, dest, visited);
                if (test != -1.0) {
                    ret_val = neighbor.value * test;
                    break;
                }
            }
        }
        visited.remove(curr);
        return ret_val;
    }

    class Pair {
        String node;
        double value;

        Pair(String node, double value) {
            this.node = node;
            this.value = value;
        }
    }
}
