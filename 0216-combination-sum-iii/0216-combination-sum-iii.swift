class Solution {
    func combinationSum3(_ k: Int, _ n: Int) -> [[Int]] {
        func backtrack(_ times: Int, _ total: Int, _ curr: inout [Int], _ visited: inout Set<Int>) {
            
            if times == k {
                if curr.reduce(0, +) == n {
                    if !res.contains(curr.sorted()) {
                        res.insert(curr)
                    }
                }
                return
            } else if total >= n {
                return
            }
            for num in 1 ... 9 {
                if !visited.contains(num) {
                    curr.append(num)
                    visited.insert(num)
                    backtrack(times + 1, total + num, &curr, &visited)
                    visited.remove(num)
                    curr.removeLast()
                }
            }
        }
        var res: Set<[Int]> = []
        var tempCurr: [Int] = []
        var visited: Set<Int> = []
        backtrack(0, 0, &tempCurr, &visited)
        return Array(res)
    }
}
