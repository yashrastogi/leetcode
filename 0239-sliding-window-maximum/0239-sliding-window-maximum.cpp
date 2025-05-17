class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        priority_queue<pair<int, int>> pq;
        for (int left = 0, right = 0; right < nums.size(); right++) {
            pq.push({nums[right], right});
            if (right - left + 1 > k) {
                left++;
                while (pq.top().second < left)
                    pq.pop();
            } else if (right - left + 1 < k) {
                continue;
            }
            res.push_back(pq.top().first);
        }
        return res;
    }
};
