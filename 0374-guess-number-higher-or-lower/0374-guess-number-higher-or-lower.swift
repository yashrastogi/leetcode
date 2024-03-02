/** 
 * Forward declaration of guess API.
 * @param  num -> your guess number
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0 
 * func guess(_ num: Int) -> Int 
 */

class Solution : GuessGame {
    func guessNumber(_ n: Int) -> Int {
        switch guess(n) {
            case 1: return binarySearch(n + 1, Int(pow(2, 31) - 1))
            case -1: return binarySearch(0, n - 1)
            default: return n
        }
    }

    func binarySearch(_ lo: Int, _ hi: Int) -> Int {
        if lo > hi {
            return -1
        }
        let mid = (lo + hi) / 2
        switch guess(mid) {
            case 1: return binarySearch(mid + 1, hi)
            case -1: return binarySearch(lo, mid - 1)
            default: return mid
        }
    }
}