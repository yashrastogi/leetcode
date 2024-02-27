#include <vector>
#include <queue>
#include <unordered_set>
#include <tuple>
#include <algorithm>

using namespace std;

class Solution {
public:
    struct PairHash {
        template <typename T1, typename T2>
        size_t operator() (const pair<T1, T2>& p) const {
            auto hash1 = hash<T1>{}(p.first);
            auto hash2 = hash<T2>{}(p.second);
            return hash1 ^ hash2;
        }
    };

    int orangesRotting(vector<vector<int>>& grid) {
        queue<tuple<int, int, int>> q;
        unordered_set<pair<int, int>, PairHash> visited;

        for (int x = 0; x < grid.size(); x++) {
            for (int y = 0; y < grid[0].size(); y++) {
                if (grid[x][y] == 2) {
                    q.push(make_tuple(x, y, 0));
                    visited.insert(make_pair(x, y));
                } else if (grid[x][y] == 0) {
                    visited.insert(make_pair(x, y));
                }
            }
        }

        int maxLevel = 0;
        vector<vector<int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        while (!q.empty()) {
            auto current = q.front();
            q.pop();
            int level = get<2>(current);
            maxLevel = max(level, maxLevel);
            visited.insert(make_pair(get<0>(current), get<1>(current)));

            if (visited.size() == grid.size() * grid[0].size()) {
                return maxLevel;
            }

            for (auto& dir : directions) {
                int newX = get<0>(current) + dir[0];
                int newY = get<1>(current) + dir[1];

                if (newX >= 0 && newX < grid.size() && newY >= 0 && newY < grid[0].size() && visited.find(make_pair(newX, newY)) == visited.end()) {
                    q.push(make_tuple(newX, newY, level + 1));
                }
            }
        }

        if (visited.size() != grid.size() * grid[0].size()) {
            return -1;
        }
        return maxLevel;
    }
};
