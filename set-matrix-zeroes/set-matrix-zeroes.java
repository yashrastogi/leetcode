class Solution {
    public void setZeroes(int[][] matrix) {
        printMatrix(matrix, 2);
        boolean clearFirstCol = false;
        for(int i=0; i<matrix.length; i++) {
            // some element in first column is zero
            if(matrix[i][0] == 0) {
                clearFirstCol = true;
            }
            
            for(int j=1; j<matrix[0].length; j++) {
                if(matrix[i][j] == 0) {
                    matrix[i][j] = -1; // not necessary just to avoid confusion
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                } 
            }
        }
        
        printMatrix(matrix, 2);
        
        for(int i=1; i<matrix.length; i++) {
            for(int j=1; j<matrix[0].length; j++) {
                if(matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }
        
        printMatrix(matrix, 2);
        
        if(matrix[0][0] == 0 && clearFirstCol) {
            for(int i=0; i<matrix.length; i++) {
                matrix[i][0] = 0;
            }
            for(int j=0; j<matrix[0].length; j++) {
                matrix[0][j] = 0;
            }
        } else if(matrix[0][0] == 0 && !clearFirstCol) {
            for(int j=0; j<matrix[0].length; j++) {
                matrix[0][j] = 0;
            }
        } else if(matrix[0][0] != 0 && clearFirstCol) {
            for(int i=0; i<matrix.length; i++) {
                matrix[i][0] = 0;
            }
        }
    }
    
    private void printMatrix(int[][] matrix, int space) {
        for(int i=0; i<matrix.length; i++) {
            System.out.print("[");
            for(int j=0; j<matrix[0].length; j++) {
                for(int x=0; x<Math.max(0,space-(""+matrix[i][j]).length()); x++) System.out.print(" ");
                System.out.print(matrix[i][j]);
                if (j != matrix[0].length-1) {
                    System.out.print(" ");
                }
            }
            System.out.println("]");
        }
        System.out.println();
    }
    
    private void print(Object o) {
        System.out.println(o);
    }
    
    private void print() {
        System.out.println();
    }
    
    private void print(Object o, String sep) {
        System.out.print(o + sep);
    }
}