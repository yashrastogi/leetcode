class Solution {
    func merge(_ intervals: [[Int]]) -> [[Int]] {
        var intervals = intervals.sorted { $0[0] < $1[0] }
        var curr = intervals[0]
        var newIntervals = [[Int]]([])
        for interval in intervals {
            if interval[0] <= curr[1] {
                curr = [min(curr[0], interval[0]), max(curr[1], interval[1])]
            } else {
                newIntervals.append(curr)
                curr = interval
            }
        }
        newIntervals.append(curr)
        return newIntervals
    }
}