class Solution {
    func combinationSum3(_ k: Int, _ n: Int) -> [[Int]] {
        func backtrack(_ total: Int, _ curr: inout [Int]) {
            if curr.count == k {
                if total == n {
                    res.append(curr)
                }
                return
            } else if total >= n {
                return
            }
            for num in (curr.last ?? 0) + 1 ..< 10 {
                curr.append(num)
                backtrack(total + num, &curr)
                curr.removeLast()
            }
        }

        var res: [[Int]] = []
        var tempCurr: [Int] = []
        backtrack(0, &tempCurr)
        return res
    }
}
