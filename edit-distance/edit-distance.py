import pprint; p = pprint.PrettyPrinter(indent=1)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # edit = [[None] * (len(word1)+1)] * (len(word2)+1)
        edit = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
        
        for i in range(len(edit)):
            edit[i][0] = i
        for i in range(len(edit[0])):
            edit[0][i] = i
            
        
        for i in range(1, len(edit)):
            for j in range(1, len(edit[0])):
                if word2[i-1] == word1[j-1]:
                    edit[i][j] = edit[i-1][j-1]
                else:
                    edit[i][j] = min(edit[i-1][j], edit[i][j-1], edit[i-1][j-1]) + 1
        
        # for row in edit: print(*row)
        return edit[-1][-1]