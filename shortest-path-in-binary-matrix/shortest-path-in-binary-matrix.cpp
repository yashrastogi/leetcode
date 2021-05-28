class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        if(grid[0][0] == 1 || grid[grid.size()-1][grid[0].size()-1] == 1) return -1;
        
        int directions[][2] = {{0,1}, {1,0}, {0,-1}, {-1,0}, {1,1}, {-1,-1}, {-1,1}, {1,-1}};
        grid[0][0] = 1;
            
        queue<array<int, 2>> q;
        q.push({0, 0});
        while(q.size() > 0) {
            auto [i, j] = q.front(); q.pop();
            if(i == grid.size()-1 && j == grid[0].size()-1) {
                return grid[i][j];
            }
            for(auto &d: directions) {
                int ix = i+d[0], jx = j+d[1];
                if (ix>=0 && jx>=0 && ix<grid.size() && jx<grid[0].size()) {
                    if(grid[ix][jx] == 0) {
                        grid[ix][jx] = grid[i][j] + 1;
                        q.push({ix, jx});
                    }
                }
            }
        }
        return -1;
    }
};