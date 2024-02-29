class Solution {
    func maxScore(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        var z = zip(nums1, nums2).sorted { $0.1 < $1.1 }
        let n = nums1.count
        var minHeap = [Int]()
        
        for i in (n - k + 1)..<n {
            heappush(&minHeap, z[i].0)
            if minHeap.count > k {
                heappop(&minHeap)
            }
        }
        
        var maxScore = -1
        for i in stride(from: n - k, through: 0, by: -1) {
            heappush(&minHeap, z[i].0)
            maxScore = max(maxScore, minHeap.reduce(0, +) * z[i].1)
            heappop(&minHeap)
        }
        return maxScore
    }
    
    private func heappush(_ heap: inout [Int], _ element: Int) {
        heap.append(element)
        var currentIndex = heap.count - 1
        var parentIndex = (currentIndex - 1) / 2
        while parentIndex >= 0 && heap[parentIndex] > heap[currentIndex] {
            heap.swapAt(parentIndex, currentIndex)
            currentIndex = parentIndex
            parentIndex = (currentIndex - 1) / 2
        }
    }
    
    private func heappop(_ heap: inout [Int]) {
        heap.swapAt(0, heap.count - 1)
        heap.removeLast()
        var currentIndex = 0
        var leftChildIndex = 1
        var rightChildIndex = 2
        while leftChildIndex < heap.count {
            var minIndex = currentIndex
            if heap[leftChildIndex] < heap[minIndex] {
                minIndex = leftChildIndex
            }
            if rightChildIndex < heap.count && heap[rightChildIndex] < heap[minIndex] {
                minIndex = rightChildIndex
            }
            if minIndex == currentIndex {
                break
            }
            heap.swapAt(currentIndex, minIndex)
            currentIndex = minIndex
            leftChildIndex = currentIndex * 2 + 1
            rightChildIndex = currentIndex * 2 + 2
        }
    }
}
