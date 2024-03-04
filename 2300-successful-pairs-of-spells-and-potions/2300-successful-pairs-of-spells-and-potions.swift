class Solution {
    func successfulPairs(_ spells: [Int], _ potions: [Int], _ success: Int) -> [Int] {
        let sortedPotions = potions.sorted()
        let searchValues = spells.map { spell in
            return Int(ceil(Double(success) / Double(spell)))
        }
        var pairs = [Int](repeating: 0, count: spells.count)

        for (index, searchVal) in searchValues.enumerated() {
            let count = sortedPotions.count - binarySearch(sortedPotions, searchVal)
            pairs[index] = count
        }
        return pairs
    }

    func binarySearch(_ array: [Int], _ search: Int) -> Int {
        var low = 0
        var high = array.count - 1
        while low <= high {
            let mid = low + (high - low) / 2
            if array[mid] < search {
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return low
    }
}
