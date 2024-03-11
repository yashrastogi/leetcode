import java.util.Arrays;

class Solution {
    int[][] dp;

    public int iterative(String text1, String text2) {
        boolean flag = false;
        int m = text1.length();
        int n = text2.length();
        for (int i = 0; i < m; i++) {
            if (text1.charAt(i) == text2.charAt(0) || flag) {
                flag = true;
                dp[i][0] = 1;
            }
        }
        flag = false;
        for (int j = 0; j < n; j++) {
            if (text1.charAt(0) == text2.charAt(j) || flag) {
                flag = true;
                dp[0][j] = 1;
            }
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (text1.charAt(i) == text2.charAt(j)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[m - 1][n - 1];
    }

    public int recursive(String text1, String text2, int i, int j) {
        if (i >= text1.length() || j >= text2.length()) {
            return 0;
        }
        if (dp[i][j] == -1) {
            if (text1.charAt(i) == text2.charAt(j)) {
                dp[i][j] = 1 + recursive(text1, text2, i + 1, j + 1);
            } else {
                dp[i][j] = Math.max(recursive(text1, text2, i + 1, j),
                        recursive(text1, text2, i, j + 1));
            }
        }
        return dp[i][j];
    }

    public int recursive(String text1, String text2) {
        return recursive(text1, text2, 0, 0);
    }

    public int longestCommonSubsequence(String text1, String text2) {
        boolean useRecursion = false;
        int m = text1.length();
        int n = text2.length();
        dp = new int[m][n];
        if (useRecursion) {
            for (int[] row : dp) {
                Arrays.fill(row, -1);
            }
            return recursive(text1, text2);
        } else {
            for (int[] row : dp) {
                Arrays.fill(row, 0);
            }
            return iterative(text1, text2);
        }
    }
}
