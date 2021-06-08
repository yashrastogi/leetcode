class Solution {
public:
    string s1, s2, s3;
    int l1, l2, l3;
    int dp[101][101][201];
    
    bool _isInterleave(int i, int j, int k) {
        if(i == l1) return s2.substr(j) == s3.substr(k);
        if(j == l2) return s1.substr(i) == s3.substr(k);
        if(dp[i][j][k] != -1) return dp[i][j][k];
        bool ans = false;
        if((s1[i] == s3[k] && _isInterleave(i + 1, j, k + 1)) || (s2[j] == s3[k] && _isInterleave(i, j + 1, k + 1))) {
            ans = true;
        }
        return dp[i][j][k] = ans;
    }
    
    bool isInterleave(string s1, string s2, string s3) {
        l1 = s1.size(); l2 = s2.size(); l3 = s3.size();
        Solution::s1 = s1; Solution::s2 = s2; Solution::s3 = s3;
        if(l3 != (l1 + l2)) return false;
        memset(dp, -1, sizeof(dp));
        return _isInterleave(0, 0, 0);   
    }
};