class Solution {
  public:
    int findDuplicate(vector<int> &nums) {
        int i = 0, j = 0;
        while (true) {
            i = nums[i];
            j = nums[nums[j]];
            if (i == j) {
                j = 0;
                while (i != j) {
                    i = nums[i];
                    j = nums[j];
                }
                return i;
            }
        }
        return 0;      
    }
};