class Solution {
    func dailyTemperatures(_ temps: [Int]) -> [Int] {
        var stack = [(Int, Int)]()
        var answer = Array(repeating: 0, count: temps.count)
        for (i, temp) in temps.enumerated() {
            while !stack.isEmpty && stack.last!.1 < temp {
                let el = stack.removeLast()
                answer[el.0] = i - el.0
            }
            stack.append((i, temp))
        }
        return answer
    }
}
