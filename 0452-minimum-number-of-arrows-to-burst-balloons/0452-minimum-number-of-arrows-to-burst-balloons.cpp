class Solution {
public:
    int findMinArrowShots(std::vector<std::vector<int>>& points) {
        std::sort(points.begin(), points.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[0] < b[0];
        });
        
        int shootArrow = 1;
        std::vector<int> curr = points[0];
        for (int i = 1; i < points.size(); i++) {
            std::vector<int>& interval = points[i];
            if (interval[0] > curr[1]) {
                shootArrow++;
                curr = interval;
            } else {
                curr[0] = std::min(curr[0], interval[0]);
                curr[1] = std::min(curr[1], interval[1]);
            }
        }
        return shootArrow;
    }
};
