class Solution {
    func numSquaresIterative(_ n: Int, _ perfectSquares: [Int]) -> Int {
        var memo: [Int] = Array(repeating: 0, count: n + 1)
        for csum in 1 ... n {
            var result = n + 1
            for sq in perfectSquares {
                if csum - sq >= 0 {
                    result = min(result, memo[csum - sq] + 1)
                }
            }
            memo[csum] = result
        }
        return memo[n]
    }

    func numSquaresRecursive(_ n: Int, _ perfectSquares: [Int]) -> Int {
        var memo: [Int] = Array(repeating: -1, count: n)
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
        let result = recursion()
        return result
    }

    func numSquares(_ n: Int) -> Int {
        var perfectSquares: [Int] = []
        for i in stride(from: Int(pow(Double(n), 1 / 2)), to: 0, by: -1) {
            perfectSquares.append(Int(pow(Double(i), 2)))
        }

        return numSquaresIterative(n, perfectSquares)
    }
}