class Solution {
public:
    int largestRectangleArea(vector<int>& h) {
        int n = h.size();
        if (n == 0)
            return 0;
        int maxArea = -INT_MAX;
        stack<int> s;
        for (int i = 0; i < n; i++) {
            while (s.size() && h[s.top()] > h[i]) {
                /*
                   enter when stack top height is greater than current index
                   height right boundary from that higher height bar is just one
                   minus index choose stack popped bar as minimum height and
                   expand left/right
                */
                int height = h[s.top()];
                s.pop();
                // index i - 1 right boundary add 1 for width
                int width = (i - 1) + 1;
                // left boundary is stack top + 1 since we popped the current
                // height bar, if empty stack no left boundary
                width -= (s.empty()) ? 0 : s.top() + 1;
                maxArea = max(maxArea, width * height);
            }
            s.push(i);
        }
        while (s.size()) {
            int height = h[s.top()];
            s.pop();
            // no right boundary for elements left in stack
            int width = n;
            width -= (s.empty()) ? 0 : s.top() + 1;
            maxArea = max(maxArea, width * height);
        }
        return maxArea;
    }
};