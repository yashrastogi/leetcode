class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int lo = 1, hi = nums.size();
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int countMid = 0;
            for(int num: nums) if(num <= mid) countMid++;
            if(countMid > mid) hi = mid - 1;
            else lo = mid + 1;
        }
        return lo;
    }
};