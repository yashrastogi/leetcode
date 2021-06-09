import pprint

class Solution:
    def minInsertions(self, s: str) -> int:
        s_ = s[::-1]
        l = len(s) + 1
        dp = [[-1] * l for _ in range(l)]
        
        for i in range(l):
            for j in range(l):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s[i - 1] == s_[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        i, j = len(s), len(s)
        SCS = []
        while i >= 1 and j >= 1:
            if s[i - 1] == s_[j - 1]:
                SCS.append(s[i - 1])
                i, j = i - 1, j - 1
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    SCS.append(s[i - 1])
                    i -= 1
                else:
                    SCS.append(s_[j - 1])
                    j -= 1 
        while i >= 1:
            SCS.append(s[i - 1])
            i -= 1
        while j >= 1:
            SCS.append(s_[j - 1])
            j -= 1
        SCS_ = ''.join(reversed(SCS))
        return len(SCS_) - len(s)
            