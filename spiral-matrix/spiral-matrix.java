class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int r1=0, r2=matrix.length-1, c1=0, c2=matrix[0].length-1;
        var ret = new ArrayList<Integer>();
        while (c1 <= c2 && r1 <= r2) {
            for(int i=c1; i<=c2; i++) {
                ret.add(matrix[r1][i]);
            }
            for(int j=r1+1; j<=r2; j++) {
                ret.add(matrix[j][c2]);
            }
            if (r1 < r2 && c1 < c2) {
                for(int k=c2-1; k>c1; k--) {
                    ret.add(matrix[r2][k]);
                }
                for(int l=r2; l>r1; l--) {
                    ret.add(matrix[l][c1]);
                }
            }
            c1++; r1++; r2--; c2--;
        }
        return ret;
    }
    public static void print(Object o) {
        print(o, "\n");
    }
    public static void print(Object o, String sep) {
        System.out.print(o + sep);
    } 
}