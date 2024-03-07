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

    func letterCombinations(_ digits: String) -> [String] {
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
}



























// func runCode() {
//     let s = Solution()
//     let outputStream = OutputStream(url: URL(fileURLWithPath: "user.out"), append: false)!
//     outputStream.open()

//     if let digitsString = readLine() {
//         let digits = try! JSONDecoder().decode(String.self, from: digitsString.data(using: .utf8)!)
//         let resultString = String(s.letterCombinations(digits).description)
//         outputStream.write(resultString, maxLength: resultString.count)
//         outputStream.write("\n", maxLength: 1)
//     }

//     outputStream.close()
//     exit(EXIT_SUCCESS)
// }

// runCode()

extension StringProtocol {
    subscript(_ offset: Int) -> Element { self[index(startIndex, offsetBy: offset)] }
    subscript(_ range: Range<Int>) -> SubSequence { prefix(range.lowerBound + range.count).suffix(range.count) }
    subscript(_ range: ClosedRange<Int>) -> SubSequence { prefix(range.lowerBound + range.count).suffix(range.count) }
    subscript(_ range: PartialRangeThrough<Int>) -> SubSequence { prefix(range.upperBound.advanced(by: 1)) }
    subscript(_ range: PartialRangeUpTo<Int>) -> SubSequence { prefix(range.upperBound) }
    subscript(_ range: PartialRangeFrom<Int>) -> SubSequence { suffix(Swift.max(0, count - range.lowerBound)) }
}

class Tools {
    class DefaultDict<Key: Hashable, Value>: CustomStringConvertible {
        private var dict: [Key: Value] = [:]
        private let defaultValue: () -> Value

        init(defaultValue: @escaping () -> Value) {
            self.defaultValue = defaultValue
        }

        subscript(key: Key) -> Value {
            get {
                if let value = dict[key] {
                    return value
                } else {
                    let defaultValue = self.defaultValue()
                    dict[key] = defaultValue
                    return defaultValue
                }
            }
            set {
                dict[key] = newValue
            }
        }

        var description: String {
            var output = "{\n"
            for (key, value) in dict {
                output += "    \(key): \(value)\n"
            }
            output += "}"
            return output
        }
    }

    public static func heapPush(_ heap: inout [(Int, Int)], _ item: (Int, Int)) {
        heap.append(item)
        var index = heap.count - 1
        while index > 0 {
            let parent = (index - 1) / 2
            if heap[parent] > heap[index] {
                heap.swapAt(parent, index)
                index = parent
            } else {
                break
            }
        }
    }

    public static func heapPop(_ heap: inout [(Int, Int)]) -> (Int, Int)? {
        guard heap.count > 0 else { return nil }
        let last = heap.removeLast()
        if !heap.isEmpty {
            let first = heap[0]
            heap[0] = last
            var index = 0
            let size = heap.count
            while index * 2 + 1 < size {
                var leftChild = index * 2 + 1
                let rightChild = leftChild + 1
                if rightChild < size, heap[rightChild] < heap[leftChild] {
                    leftChild = rightChild
                }
                if heap[leftChild] < heap[index] {
                    heap.swapAt(leftChild, index)
                    index = leftChild
                } else {
                    break
                }
            }
            return first
        } else {
            return last
        }
    }
}
