class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        return binarySearch(matrix, target, 0, (matrix.length * matrix[0].length) - 1);
    }

    public int[] indexMapper(int i, int[][] matrix) {
        return new int[]{i / matrix[0].length, i % matrix[0].length};
    }

    public boolean binarySearch(int[][] matrix, int target, int lo, int hi) {
        if (lo > hi) {
            return false;
        }
        int mid = (hi - lo) / 2 + lo;
        int[] ix = indexMapper(mid, matrix);
        if (matrix[ix[0]][ix[1]] == target) {
            return true;
        } else if (matrix[ix[0]][ix[1]] < target) {
            return binarySearch(matrix, target, mid + 1, hi);
        } else {
            return binarySearch(matrix, target, lo, mid - 1);
        }
    }
}
