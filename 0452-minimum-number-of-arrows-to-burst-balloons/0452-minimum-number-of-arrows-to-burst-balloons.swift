class Solution {
    func findMinArrowShots(_ points: [[Int]]) -> Int {
        var points = points.sorted {$0[0] < $1[0]}
        var shootArrow = 1
        var curr = points[0]
        for interval in points.dropFirst() {
            if interval[0] > curr[1] {
                shootArrow += 1
                curr = interval
            } else {
                curr = [min(curr[0], interval[0]), min(curr[1], interval[1])]
            }
        }
        return shootArrow
    }
}