class Solution : GuessGame {
    func guessNumber(_ n: Int) -> Int {
        switch guess(n) {
            case -1: return binarySearch(0, n - 1)
            default: return n
        }
    }

    func binarySearch(_ lo: Int, _ hi: Int) -> Int {
        let mid = (lo + hi) / 2
        switch guess(mid) {
            case 1: return binarySearch(mid + 1, hi)
            case -1: return binarySearch(lo, mid - 1)
            default: return mid
        }
    }
}