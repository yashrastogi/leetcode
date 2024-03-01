class Solution {
    func totalCost(_ costs: [Int], _ k: Int, _ candidates: Int) -> Int {
        var totalCost = 0
        var heap = [(Int, Int)]()
        var p1 = 0
        var p2 = costs.count - 1

        while p1 < candidates {
            heappush(&heap, (costs[p1], p1))
            p1 += 1
        }

        while p2 >= costs.count - candidates && p2 >= p1 {
            heappush(&heap, (costs[p2], p2))
            p2 -= 1
        }

        for _ in 0 ..< k {
            guard let minElement = heappop(&heap) else { break }
            totalCost += minElement.0

            if minElement.1 < p1 && p1 <= p2 {
                heappush(&heap, (costs[p1], p1))
                p1 += 1
            } else if p2 >= p1 {
                heappush(&heap, (costs[p2], p2))
                p2 -= 1
            }
        }
        return totalCost
    }

    func heappush(_ heap: inout [(Int, Int)], _ item: (Int, Int)) {
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

    func heappop(_ heap: inout [(Int, Int)]) -> (Int, Int)? {
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
