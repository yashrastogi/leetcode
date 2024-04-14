class Solution {
    func isValid(_ s: String) -> Bool {
        var stack: [Character] = []
        let start: [Character: Character] = ["(": ")", "{": "}", "[": "]"]
        for c in s {
            if start.keys.contains(c) {
                stack.append(c)
            } else if stack.isEmpty || start[stack.removeLast()] != c { 
                return false
            }
        }
        return stack.isEmpty
    }
}