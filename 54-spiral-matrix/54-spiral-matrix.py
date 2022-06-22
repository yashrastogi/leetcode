class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        L_B, U_B = 0, 0
        D_B, R_B = len(matrix), len(matrix[0])
        res = []
        while len(res) < len(matrix) * len(matrix[0]):
            for i in range(L_B, R_B):
                res.append(matrix[U_B][i])
            # print(res,1)
            for i in range(U_B + 1, D_B):
                res.append(matrix[i][R_B-1])
            # print(res,2)
            if len(res) >= len(matrix) * len(matrix[0]):
                break
            for i in reversed(range(L_B, R_B-1)):
                res.append(matrix[D_B-1][i])
            # print(res,3)
            for i in reversed(range(U_B+1, D_B-1)):
                res.append(matrix[i][L_B])
            U_B += 1
            R_B -= 1
            L_B += 1
            D_B -= 1
            # print(res)
        return res