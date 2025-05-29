
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
        for (int i = n - 1; i >= 0; i--) {
            while (monoDec.size() && heights[monoDec.top()] > heights[i]) {
                int j = monoDec.top(); // index j's left boundary is i + 1
                int leftBoundary = i + 1;
                int rightBoundary = (right[j] == -1) ? n - 1 : right[j];
                maxArea = max(maxArea, (rightBoundary - leftBoundary + 1) * heights[j]);
                monoDec.pop();
            }
            monoDec.push(i);
        }

        while(monoDec.size()) {
            int j = monoDec.top();
            int leftBoundary = 0;
            int rightBoundary = (right[j] == -1) ? n - 1 : right[j];
            maxArea = max(maxArea, (rightBoundary - leftBoundary + 1) * heights[j]);
            monoDec.pop();
        }

        return maxArea;
    }
};