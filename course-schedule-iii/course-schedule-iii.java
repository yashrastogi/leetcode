class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, (a, b) -> a[1] - b[1]);
        // print(Arrays.deepToString(courses));
        var pq = new PriorityQueue<Integer>(Collections.reverseOrder());
        int timeElapsed = 0;
        for(var c: courses) {
            if (timeElapsed + c[0] <= c[1]) {
                timeElapsed += c[0];
                pq.add(c[0]);
            } else if(!pq.isEmpty() && pq.peek() > c[0]) {
                timeElapsed += c[0] - pq.poll();
                pq.add(c[0]);
            }
        }
        return pq.size();
    }
     
    public static void print(Object o, String sep) {
        System.out.print(o + sep);
    }
    public static void print(Object o) {
        print(o, "\n");
    }
}