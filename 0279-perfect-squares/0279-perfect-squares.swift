class Solution {
    func numSquares(_ n: Int) -> Int {
        var memo: [Int] = Array(repeating: -1, count: n + 1)
        var perfectSquares: [Int] = []
        
        func recursion(_ csum: Int = 0) -> Int {
            guard csum <= n else { return n + 1 }
            if csum == n { return 0 }
            if memo[csum] != -1 { return memo[csum] }
            var result = n + 1
            for sq in perfectSquares { 
                result = min(result, 1 + recursion(csum + sq))
            }
            memo[csum] = result
            return result
        }
            
        for i in stride(from: Int(pow(Double(n), 1/2)), to: 0, by: -1) {
            perfectSquares.append(Int(pow(Double(i), 2)))
        }
        return recursion()
    }
}