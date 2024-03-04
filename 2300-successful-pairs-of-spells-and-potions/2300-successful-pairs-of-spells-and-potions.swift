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
            let closeIdx = binarySearch(searchVal, potions)
            count += potions.count - closeIdx
            pairs.append(count)
        }
        return pairs
    }

    func binarySearch(_ search: Int, _ array: [Int]) -> Int {
        var lo = 0
        var hi = array.count - 1
        while lo <= hi {
            let mid = lo + (hi - lo) / 2
            if array[mid] < search {
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return lo
    }
}
