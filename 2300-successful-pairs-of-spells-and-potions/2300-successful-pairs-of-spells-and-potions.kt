class Solution {
    fun successfulPairs(spells: IntArray, potions: IntArray, success: Long): IntArray {
        val sortedPotions = potions.sortedArray()
        val searchValues = spells.map { ceil(success.toDouble() / it).toInt() }
        val pairs = IntArray(spells.size)

        for ((index, searchVal) in searchValues.withIndex()) {
            val count = sortedPotions.size - binarySearch(sortedPotions, searchVal)
            pairs[index] = count
        }
        return pairs
    }

    private fun binarySearch(array: IntArray, search: Int): Int {
        var low = 0
        var high = array.size - 1
        while (low <= high) {
            val mid = low + (high - low) / 2
            if (array[mid] < search) {
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return low
    }
}
