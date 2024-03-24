class Solution {
    func partition(_ s: String) -> [[String]] {
        var result: [[String]] = []
        var currentList: [String] = []
        
        backtrack(s, &result, &currentList, 0)
        
        return result
    }
    
    func backtrack(_ s: String, _ result: inout [[String]], _ currentList: inout [String], _ start: Int) {
        if start == s.count {
            result.append(currentList)
            return
        }
        
        for end in start..<s.count {
            if isPalindrome(s, start, end) {
                let substring = String(s[s.index(s.startIndex, offsetBy: start)...s.index(s.startIndex, offsetBy: end)])
                currentList.append(substring)
                backtrack(s, &result, &currentList, end + 1)
                currentList.removeLast()
            }
        }
    }
    
    func isPalindrome(_ s: String, _ left: Int, _ right: Int) -> Bool {
        var leftIndex = left
        var rightIndex = right
        
        while leftIndex < rightIndex {
            if s[s.index(s.startIndex, offsetBy: leftIndex)] != s[s.index(s.startIndex, offsetBy: rightIndex)] {
                return false
            }
            leftIndex += 1
            rightIndex -= 1
        }
        
        return true
    }
}
