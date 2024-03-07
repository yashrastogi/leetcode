class Solution {
    var lookup: [Character: [String]] = [
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    ]

    func letterCombinations(_ digits: String) -> [String] {
        func backtrack(_ i: Int, _ curr: inout String, _ res: inout [String]) {
            if i == digits.count {
                res.append(curr)
                return
            }
            for ch in lookup[digits[i]]! {
                curr += ch
                backtrack(i + 1, &curr, &res)
                curr.removeLast()
            }
        }
        if digits.count < 1 {
            return []
        }
        var res: [String] = []
        var tempString = ""
        backtrack(0, &tempString, &res)
        return res
    }
}

extension StringProtocol {
    subscript(_ offset: Int) -> Element { self[index(startIndex, offsetBy: offset)] }
    subscript(_ range: Range<Int>) -> SubSequence { prefix(range.lowerBound + range.count).suffix(range.count) }
    subscript(_ range: ClosedRange<Int>) -> SubSequence { prefix(range.lowerBound + range.count).suffix(range.count) }
    subscript(_ range: PartialRangeThrough<Int>) -> SubSequence { prefix(range.upperBound.advanced(by: 1)) }
    subscript(_ range: PartialRangeUpTo<Int>) -> SubSequence { prefix(range.upperBound) }
    subscript(_ range: PartialRangeFrom<Int>) -> SubSequence { suffix(Swift.max(0, count - range.lowerBound)) }
}
