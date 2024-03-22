class Solution {
    func merge(_ intervals: [[Int]]) -> [[Int]] {
        var intervals = intervals.sorted { $0[0] < $1[0] }
        var start = intervals[0][0], end = intervals[0][1]
        var newIntervals = [[Int]]([])
        for interval in intervals {
            if interval[0] <= end {
                start = min(start, interval[0])
                end = max(end, interval[1])
            } else if interval[0] > end {
                newIntervals.append([start, end])
                start = interval[0]
                end = interval[1]
            }
        }
        newIntervals.append([start, end])
        return newIntervals
    }
}