class Solution {
public:
    vector<vector<int>> dp;

    int iterative(string text1, string text2) {
        bool flag = false;
        for (int i = 0; i < text1.size(); i++) {
            if (text1[0] == text2[0] || text1[i] == text2[0]) {
                flag = true;
            }
            if (flag) {
                dp[i][0] = 1;
            }
        }
        flag = false;
        for (int j = 0; j < text2.size(); j++) {
            if (text1[0] == text2[0] || text1[0] == text2[j]) {
                flag = true;
            }
            if (flag) {
                dp[0][j] = 1;
            }
        }
        for (int i = 1; i < text1.size(); i++) {
            for (int j = 1; j < text2.size(); j++) {
                if (text1[i] == text2[j]) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[text1.size() - 1][text2.size() - 1];
    }

    int recursive(string text1, string text2, int i = 0, int j = 0) {
        if (i >= text1.size() || j >= text2.size()) {
            return 0;
        }
        if (dp[i][j] == -1) {
            if (text1[i] == text2[j]) {
                dp[i][j] = 1 + recursive(text1, text2, i + 1, j + 1);
            } else {
                dp[i][j] = max(recursive(text1, text2, i + 1, j),
                               recursive(text1, text2, i, j + 1));
            }
        }
        return dp[i][j];
    }

    int longestCommonSubsequence(string text1, string text2) {
        bool useRecursion = false;
        int ans = 0;
        if (useRecursion) {
            dp = vector<vector<int>>(text1.size(), vector<int>(text2.size(), -1));
            ans = recursive(text1, text2);
        } else {
            dp = vector<vector<int>>(text1.size(), vector<int>(text2.size(), 0));
            ans = iterative(text1, text2);
        }
        return ans;
    }
};