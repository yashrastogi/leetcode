class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lenm = len(m)
        # algorithm to transpose square matrix in place, swap all elements in left of diagonal with right of diagonal
        for i in range(lenm):
            for j in range(0,i):
                temp = m[i][j]
                m[i][j] = m[j][i]
                m[j][i] = temp

        # reverse every row in matrix
        for i in range(lenm):
            for j in range(int(lenm/2)):
                temp = m[i][j]
                m[i][j] = m[i][lenm-1-j]
                m[i][lenm-1-j] = temp
                