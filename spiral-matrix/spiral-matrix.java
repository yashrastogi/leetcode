class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        var ret = new ArrayList<Integer>();
        int c1=0, c2=matrix[0].length, r1=0, r2=matrix.length;
        while(c1 < c2 && r1 < r2) {
            for(int c=c1; c<c2; c++) {
                // System.out.println("1 " + matrix[r1][c]);
                ret.add(matrix[r1][c]);
            }
            for(int r=r1+1; r<r2; r++) {
                // System.out.println("2 " + matrix[r][c2-1]);
                ret.add(matrix[r][c2-1]);
            }
            if(c1 < c2-1 && r1 < r2-1){
            for(int c=c2-1-1; c>=c1; c--) {
                // System.out.println("3 " + matrix[r2-1][c]);
                ret.add(matrix[r2-1][c]);
            }
            for(int r=r2-1-1; r>=r1+1; r--) {
                // System.out.println("4 " + matrix[r][c1]);
                ret.add(matrix[r][c1]);
            }}
            c1++; c2--;
            r1++; r2--;
        }
        return ret;
    }
}