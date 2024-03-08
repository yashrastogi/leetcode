class Solution {
    func combinationSum3(_ k: Int, _ n: Int) -> [[Int]] {
        func backtrack(_ times: Int, _ total: Int, _ curr: inout [Int]) {
            if times == k {
                if total == n {
                    res.append(curr)
                }
                return
            } else if total >= n {
                return
            }
            for num in (curr.last ?? 0) + 1 ..< 10 {
                curr.append(num)
                backtrack(times + 1, total + num, &curr)
                curr.removeLast()
            }
        }

        var res: [[Int]] = []
        var tempCurr: [Int] = []
        backtrack(0, 0, &tempCurr)
        return res
    }
}
