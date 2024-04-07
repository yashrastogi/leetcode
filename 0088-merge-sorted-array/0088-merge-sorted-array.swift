class Solution {
    func merge(_ nums1: inout [Int], _ m: Int, _ nums2: [Int], _ n: Int) {
        var i = 0, j = 0
        var rebuilt = [Int]()
        while i < m || j < n {
            if i == m {
                rebuilt.append(nums2[j])
                j += 1
            } else if j == n || nums1[i] < nums2[j] {
                rebuilt.append(nums1[i])
                i += 1
            } else {
                rebuilt.append(nums2[j])
                j += 1
            }

        }
        nums1 = rebuilt
    }
}