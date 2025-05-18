class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res(nums.size() - k + 1);
        deque<int> dq;
        for (int left = 0, right = 0; right < nums.size(); right++) {
            while (dq.size() > 0 && nums[right] >= nums[dq.back()]) 
                dq.pop_back();
            dq.push_back(right);
            if (right - left + 1 > k) 
                left++;
            else if (right - left + 1 < k) 
                continue;
            while (dq.front() < left)
                dq.pop_front();
            res[left] = nums[dq.front()];
        }
        return res;
    }
};
