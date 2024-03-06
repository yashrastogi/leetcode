class Solution {
    func findPeakElement(_ nums: [Int]) -> Int {
        var lo = 0
        var hi = nums.count - 1
        while lo < hi {
            let mid = (hi - lo) / 2 + lo
            if nums[mid] < nums[mid + 1] {
                lo += 1
            } else {
                hi -= 1
            }
        }
        return lo
    }
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
