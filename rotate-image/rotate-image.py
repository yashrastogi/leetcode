class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lenm = len(m)
        for i in range(lenm):
            for j in range(i+1,lenm):
                temp = m[i][j]
                m[i][j] = m[j][i]
                m[j][i] = temp
        for coli in range(lenm):
            m[coli] = m[coli][::-1]