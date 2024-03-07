import Foundation

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

    func backtrack(_ digits: [Character], _ idx: Int, _ curr: [String]) -> [String] {
        if idx == digits.count {
            return curr
        }
        var ret: [String] = []
        for c in curr {
            for char in lookup[digits[idx]]! {
                ret.append(c + char)
            }
        }
        return backtrack(digits, idx + 1, ret)
    }

    func letterCombinations(_ digits: String) -> [String] {
        if digits.count < 1 {
            return []
        }
        return backtrack(Array(digits), 0, [""])
    }
}
