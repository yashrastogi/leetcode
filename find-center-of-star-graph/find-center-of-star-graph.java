class Solution {
    public int findCenter(int[][] edges) {
        var counter = new HashMap<Integer, Integer>();
        for (var edge: edges) {
            for (var vert: edge) {
                counter.put(vert, counter.getOrDefault(vert, 0) + 1);
            }
        }
        for (var en: counter.entrySet()) {
            if (en.getValue() == edges.length) {
                return en.getKey();        
            }
        }
        return -1;
    }
    
    public void print(Object o, String sep) {
        System.out.print(o + sep);        
    }
    public void print(Object o) {
        print(o, "\n");
    }
    public void print() {
        print("");
    }
}