class Solution {
    func successfulPairs(_ spells: [Int], _ potions: [Int], _ success: Int) -> [Int] {
        var pairs = [Int]()
        let potions = potions.sorted()
        for spell in spells {
            var count = 0
            let searchVal = Int(ceil(Double(success) / Double(spell)))
            if potions[potions.count - 1] < searchVal {
                pairs.append(0)
                continue
            }
            let closeIdx = binarySearch(0, potions.count - 1, searchVal, potions)
            count += potions.count - closeIdx
            pairs.append(count)
        }
        return pairs
    }

    func binarySearch(_ lo: Int, _ hi: Int, _ search: Int, _ array: [Int]) -> Int {
        if lo > hi {
            return hi + 1
        }
        var mid = (lo + hi) / 2
        if array[mid] < search {
            return binarySearch(mid + 1, hi, search, array)
        }
        else {
            return binarySearch(lo, mid - 1, search, array)
        }
    }
}
