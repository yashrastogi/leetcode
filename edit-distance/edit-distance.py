class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        edit = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
        
        for i in range(max(len(edit), len(edit[0]))):
            if i < len(edit): edit[i][0] = i
            if i < len(edit[0]): edit[0][i] = i
            
        
        for i in range(1, len(edit)):
            for j in range(1, len(edit[0])):
                if word2[i-1] == word1[j-1]: edit[i][j] = edit[i-1][j-1]
                
                else: edit[i][j] = min(edit[i-1][j], edit[i][j-1], edit[i-1][j-1]) + 1
        
        
        return edit[-1][-1]