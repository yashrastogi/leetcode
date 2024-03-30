class Solution {
    func nextGreatestLetter(_ letters: [Character], _ target: Character) -> Character {
        func binarySearch(_ lo: Int, _ hi: Int) -> Character {
            guard lo < letters.count else {
                return letters[0]
            }
            guard lo <= hi else {
                return letters[lo]
            }
            let mid = (lo + hi) / 2
            if letters[mid] > target {
                return binarySearch(lo, mid - 1)
            }
            return binarySearch(mid + 1, hi)
        }

        return binarySearch(0, letters.count - 1)
    }
}