class Solution {
    func maxScore(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        let z = zip(nums1, nums2).sorted { $0.1 < $1.1 }
        let n = nums1.count
        var minHeap = [Int]()
        var maxScore = -1
        var sum = 0
        for i in (0 ..< n).reversed() {
            heappush(&minHeap, z[i].0)
            sum += z[i].0
            if minHeap.count > k {
                sum -= heappop(&minHeap)
            }
            if (n-i) >= k {
                maxScore = max(maxScore, sum * z[i].1)
            }
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
    
    private func heappop(_ heap: inout [Int]) -> Int {
        heap.swapAt(0, heap.count - 1)
        let ret = heap.removeLast()
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
        return ret
    }
}