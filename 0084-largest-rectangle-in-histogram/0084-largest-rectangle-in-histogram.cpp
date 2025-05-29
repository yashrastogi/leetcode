
class Solution {
   public:
    int largestRectangleArea(vector<int>& heights) {
        if (!heights.size()) return 0;
        int n = heights.size();
        int maxArea = -INT_MAX;
        vector<int> right(n, -1);
        stack<int> monoDec;
        for (int i = 0; i < n; i++) {
            while (monoDec.size() && heights[monoDec.top()] > heights[i]) {
                right[monoDec.top()] = i - 1;
                monoDec.pop();
            }
            monoDec.push(i);
        }
        while (monoDec.size()) monoDec.pop();
        vector<int> left(n, -1);
        for (int i = n - 1; i >= 0; i--) {
            while (monoDec.size() && heights[monoDec.top()] > heights[i]) {
                left[monoDec.top()] = i + 1;
                monoDec.pop();
            }
            monoDec.push(i);
        }
        for (int i = 0; i < n; i++) {
            int righti = right[i], lefti = left[i];
            if (righti == -1) righti = heights.size() - 1;
            if (lefti == -1) lefti = 0;
            int width = righti - lefti + 1;
            maxArea = max(maxArea, width * heights[i]);
        }

        return maxArea;
    }
};