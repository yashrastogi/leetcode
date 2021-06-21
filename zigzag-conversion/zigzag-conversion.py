from pprint import pprint

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        numRows = min(numRows, len(s))
        ret = [[] for _ in range(numRows)]
        j = 0
        down = True
        for i in range(len(s)):
            ret[j] += [s[i]]
            j += 1 if down else -1
            if j == numRows - 1 or j == 0: down = not down
        
        return ''.join([''.join(row) for row in ret])