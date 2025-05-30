class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        nums1.insert(nums1.end(), nums2.begin(), nums2.end());
        sort(nums1.begin(), nums1.end());
        int mid = nums1.size() / 2;
        if(nums1.size() % 2 == 0) {
            return ((double) nums1[mid] + nums1[mid - 1]) / 2;
        } else {
            return nums1[mid];
        }
    }
};
