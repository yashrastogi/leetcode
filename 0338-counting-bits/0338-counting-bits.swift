class Solution {
    func countBits(_ n: Int) -> [Int] {
        var ans = Array(repeating: 0, count: n + 1)
        for i in 0 ... n {
            var temp = i
            var oneCount = 0
            while temp != 0 {
                oneCount += temp & 1
                temp >>= 1
            }
            ans[i] = oneCount
        }
        return ans
    }
}