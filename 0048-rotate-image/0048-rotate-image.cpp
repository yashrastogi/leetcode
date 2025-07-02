class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        for(int row = 0; row < matrix.size(); row++) { 
            for(int col = row + 1; col < matrix[row].size(); col++) { 
                int temp = matrix[row][col];
                matrix[row][col] = matrix[col][row];
                matrix[col][row] = temp;
            }
            reverse(matrix[row].begin(), matrix[row].end());
        }
    }
};
