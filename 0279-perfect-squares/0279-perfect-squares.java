class Solution {
    public int numSquares(int n) {
        int[] perfectSquares = new int[(int) Math.sqrt(n)];
        for (int i = (int) Math.sqrt(n); i > 0; i--) {
            perfectSquares[(int) Math.sqrt(n) - i] = (int) Math.pow(i, 2);
        }
        return numSquaresRecursive(n, perfectSquares);
    }

    public int numSquaresIterative(int n, int[] perfectSquares) {
        int[] memo = new int[n + 1];
        Arrays.fill(memo, n + 1);
        memo[0] = 0;

        for (int csum = 1; csum <= n; csum++) {
            int result = n + 1;
            for (int sq : perfectSquares) {
                if (csum - sq >= 0) {
                    result = Math.min(result, memo[csum - sq] + 1);
                }
            }
            memo[csum] = result;
        }

        return memo[n];
    }

    public int numSquaresRecursive(int n, int[] perfectSquares) {
        int[] memo = new int[n];
        Arrays.fill(memo, -1);

        return recursion(0, n, perfectSquares, memo);
    }

    private int recursion(int csum, int n, int[] perfectSquares, int[] memo) {
        if (csum > n)
            return n + 1;
        if (csum == n)
            return 0;
        if (memo[csum] != -1)
            return memo[csum];

        int result = n + 1;
        for (int sq : perfectSquares) {
            result = Math.min(result, 1 + recursion(csum + sq, n, perfectSquares, memo));
        }

        memo[csum] = result;
        return result;
    }
}
