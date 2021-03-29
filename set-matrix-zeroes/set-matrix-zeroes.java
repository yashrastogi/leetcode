class Solution {
    public class Tuple<X, Y> {
        public final X x;
        public final Y y;
        public Tuple(X x, Y y) {
            this.x = x;
            this.y = y;
        }
        public int hashCode() {
            return this.x.hashCode() ^ this.y.hashCode();
        }
        public String toString() {
            return "(" + this.x + ", " + this.y + ")";
        }
    }
    
    public void setZeroes(int[][] matrix) {
        var zeroRows = new HashSet<Integer>();
        var zeroCols = new HashSet<Integer>();
        for(int i=0; i<matrix.length; i++) {
            for(int j=0; j<matrix[i].length; j++) {
                if (matrix[i][j] == 0) {
                    zeroRows.add(i);
                    zeroCols.add(j);
                }
            }
        }
        for(int i: zeroRows) {
            for(int j=0; j<matrix[i].length; j++) matrix[i][j] = 0;
        }
        for(int j: zeroCols) {
            for(int i=0; i<matrix.length; i++) matrix[i][j] = 0;
        }
    } 
    
    public static void print(Object o, String sep) {
        System.out.print(o + sep);
    }   
    public static void print(Object o) {
        print(o, "\n");
    }
}