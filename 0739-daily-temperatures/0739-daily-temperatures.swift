class Solution {
    func dailyTemperatures(_ temps: [Int]) -> [Int] {
        var stack = [Int]()
        var answer = Array(repeating: 0, count: temps.count)
        for (i, temp) in temps.enumerated() {
            while let last = stack.last, temps[last] < temp {
                let j = stack.removeLast()
                answer[j] = i - j
            }
            stack.append(i)
        }
        return answer
    }
}
