from pprint import pprint

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # pprint(matrix)
        self.transpose(matrix)
        # pprint(matrix)
        self.reflect(matrix)
        # pprint(matrix)
    
    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
    def reflect(self, matrix):
        for i in range(len(matrix)):
            lo, hi = 0, len(matrix[0]) - 1
            while lo < hi:
                temp = matrix[i][lo]
                matrix[i][lo] = matrix[i][hi]
                matrix[i][hi] = temp
                lo += 1
                hi -= 1
        