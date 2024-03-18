class Solution {
    func dailyTemperatures(_ temps: [Int]) -> [Int] {
        var answer = Array(repeating: 0, count: temps.count)
        for i in 0 ..< temps.count {
            for j in i ..< temps.count {
                if temps[j] > temps[i] {
                    answer[i] = j - i
                    break
                }
            }
        }
        return answer
    }
}