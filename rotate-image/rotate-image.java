class Solution {
    public void rotate(int[][] matrix) {
        for(int i=0; i<matrix.length; i++) {
            for(int j=i+1; j<matrix[0].length; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        
        for(int j=0; j<matrix.length; j++) {
            var row = matrix[j];
            int[] revRow = new int[row.length];
            for(int i=0; i<row.length; i++) {
                revRow[row.length-1-i] = row[i];
            }
            matrix[j] = revRow;
        }
    }
}