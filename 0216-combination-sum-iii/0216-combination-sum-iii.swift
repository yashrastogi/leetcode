class Solution {
    func combinationSum3(_ k: Int, _ n: Int) -> [[Int]] {
        func backtrack(_ times: Int, _ total: Int, _ start: Int, _ curr: inout [Int]) {
            if times == k {
                if total == n {
                    res.append(curr)
                }
                return
            } else if start > 9 || total >= n { 
                return
            }
            for num in start ... 9 {
                curr.append(num)
                backtrack(times + 1, total + num, num + 1, &curr)
                curr.removeLast()
            }
        }
        var res: [[Int]] = []
        var tempCurr: [Int] = []
        backtrack(0, 0, 1, &tempCurr)
        return res
    }
}
