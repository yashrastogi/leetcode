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

    func letterCombinations(_ digits: [Character]) -> [String] {
        func backtrack(_ idx: Int, _ curr: [String]) -> [String] {
            if idx == digits.count {
                return curr
            }
            var ret: [String] = []
            for c in curr {
                for char in lookup[digits[idx]]! {
                    ret.append(c + char)
                }
            }
            return backtrack(idx + 1, ret)
        }

        if digits.count < 1 {
            return []
        }
        return backtrack(0, [""])
    }

    func letterCombinations(_ digits: String) -> [String] {
        return letterCombinations(Array(digits))
    }
}