class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        val theSet = mutableSetOf<Int>()
        for (num in nums) {
            if (theSet.contains(num)) {
                return true
            } else {
                theSet.add(num)
            }
        }
        return false
    }
}