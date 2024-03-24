class Solution {
    func partition(_ s: String) -> [[String]] {
        var s = Array(s)
        func backtrack(_ i: Int = 0) {
            guard i < s.count else {
                ret.append(temp)
                return
            }
            for len in 0..<(s.count - i) {
                let builtString = String(s[i...i + len])
                if isPalindrome(builtString) {
                    temp.append(builtString)
                    backtrack(i + len + 1)
                    temp.removeLast()
                }
            }
        }

        var temp = [String]()
        var ret = [[String]]()
        backtrack()
        return ret
    }

    func isPalindrome(_ string: String) -> Bool {
        return String(string.reversed()) == string
    }
}