class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1, j = n - 1, ins = m + n - 1;
        while (i >= 0 || j >= 0) {
            if (i == -1) {
                nums1[ins] = nums2[j];
                j--;
            } else if (j == -1 || nums1[i] > nums2[j]) {
                nums1[ins] = nums1[i];
                i--;
            } else {
                nums1[ins] = nums2[j];
                j--;
            }
            ins--;
        }
    }
}
