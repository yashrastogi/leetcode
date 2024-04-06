class Solution {
  func search(_ nums: [Int], _ target: Int) -> Bool {
    var lo = 0, hi = nums.count - 1
    while lo <= hi {
      let mid = (lo + hi) / 2
      if nums[mid] == target {
        return true
      } else if nums[lo] == nums[mid] && nums[hi] == nums[mid] {
        lo += 1
        hi -= 1
      } else if nums[lo] <= nums[mid] {
        if target < nums[mid] && target >= nums[lo] {
          hi = mid - 1
        } else {
          lo = mid + 1
        }
      } else {
        if target > nums[mid] && target <= nums[hi] {
          lo = mid + 1
        } else {
          hi = mid - 1
        }
      }
    }
    return false
  }
}