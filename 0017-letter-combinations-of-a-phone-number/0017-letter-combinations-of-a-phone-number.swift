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
        func backtrack(_ i: Int, _ curr: String) {
            if i == digits.count {
                res.append(curr)
                return
            }
            var curr = curr
            for ch in lookup[digits[i]]! {
                curr += ch
                backtrack(i + 1, curr)
                curr.removeLast()
            }
        }
        var res: [String] = []
        backtrack(0, "")
        return res
    }

    func letterCombinations(_ digits: String) -> [String] {
        if digits.count < 1 {
            return []
        }
        return letterCombinations(Array(digits))
    }
}
