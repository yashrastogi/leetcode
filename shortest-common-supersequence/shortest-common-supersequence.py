class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1) + 1, len(str2) + 1
        dp = [[-1] * l2 for _ in range(l1)]
        
        for i in range(l1):
            for j in range(l2):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        string_list = []
        i, j = len(str1), len(str2)
        while i >= 1 and j >= 1:
            if str1[i - 1] == str2[j - 1]:
                string_list.append(str1[i - 1])
                i, j = i - 1, j - 1
            else:
                if dp[i][j - 1] > dp[i - 1][j]:
                    string_list.append(str2[j - 1])
                    j -= 1
                else:
                    string_list.append(str1[i - 1])
                    i -= 1
        
        while i >= 1:
            string_list.append(str1[i - 1])
            i -= 1
        while j >= 1:
            string_list.append(str2[j - 1])
            j -= 1
                
        
        return ''.join(reversed(string_list))
                