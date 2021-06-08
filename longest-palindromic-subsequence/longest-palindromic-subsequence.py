import pprint

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2 = s[::-1]
        l1, l2 = len(s) + 1, len(s) + 1
        
        dp = [[-1] * l2 for _ in range(l1)]
        
        for i in range(l1):
            for j in range(l2):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]
#         lcs = []
#         i, j =len(s), len(s)
#         while i>=1 and j>=1:
#             if s[i - 1] == s2[j - 1]:
#                 lcs.append(s[i - 1])
#                 i -= 1
#                 j -= 1
#             else:
#                 if dp[i - 1][j] > dp[i][j - 1]:
#                     i -= 1
#                 else:
#                     j -= 1
                    
#         return ''.join(reversed(lcs))
        
