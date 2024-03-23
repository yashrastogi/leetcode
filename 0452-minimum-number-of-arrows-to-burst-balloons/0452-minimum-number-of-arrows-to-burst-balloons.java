class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, (a, b) -> Integer.compare(a[0], b[0]));
        int shootArrow = 1;
        int[] curr = points[0];
        for (int i = 1; i < points.length; i++) {
            int[] interval = points[i];
            if (interval[0] > curr[1]) {
                shootArrow++;
                curr = interval;
            } else {
                curr[0] = Math.min(curr[0], interval[0]);
                curr[1] = Math.min(curr[1], interval[1]);
            }
        }
        return shootArrow;
    }
}
