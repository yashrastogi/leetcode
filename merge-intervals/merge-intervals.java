class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt((x) -> x[0]));
        
        var ret = new ArrayList<int[]>();
        
        for (int i=0; i<intervals.length; i++) {
            int start = intervals[i][0], end = intervals[i][1];
            for(int j=i+1; j<intervals.length; j++) {
                if(intervals[j][0] <= end) {
                    end = Math.max(intervals[j][1], end);
                    i = j;
                }
            }
            ret.add(new int[] {start, end});
        }
        var retArr = new int[ret.size()][2];
        for(int i=0; i<retArr.length; i++) {
            retArr[i] = ret.get(i);
        }
        return retArr;
    }
}