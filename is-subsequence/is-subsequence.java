class Solution {
    public boolean isSubsequence(String s, String t) {
        int l1 = s.length(), l2 = t.length();
        if(l1 == 0 && l2 == 0) return true;
        if(l2 == 0) return false;
        var dp = new int[l1 + 1][l2 + 1];
        for(int i=0; i <= l1; i++)
        {
            for(int j=0; j <= l2; j++)
            {
                if(i == 0 || j == 0)
                    dp[i][j] = 0;
                else if(s.charAt(i - 1) == t.charAt(j - 1))
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                else
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[l1][l2] == l1;
    }
}