class SmallestInfiniteSet
{
    var heap: MinPriorityQueue<Int>
    var sn: Int

    init() {
        heap = MinPriorityQueue()
        sn = 1
    }
    
    func popSmallest() -> Int 
    {
        if let dequeuedValue = heap.dequeue() {
            return dequeuedValue
        } else {
            sn += 1
            return sn - 1
        }
    }
    
    func addBack(_ num: Int)
    {
        if num < sn {
            heap.add(num)
        }        
    }
}

protocol Queue
{
    associatedtype DataType: Comparable
    @discardableResult func add(_ item: DataType) -> Bool  // Inserts a new item into the queue, if it does not already contain one
    @discardableResult func remove() -> DataType?  // Removes the first item in line, if there is one
    func dequeue() -> DataType?   // Gets the first item in line and removes it from the queue
    func peek() -> DataType?  // Gets the first item in line, without removing it from the queue
    func contains(_ item: DataType) -> Bool // Reports if the queue contains item
    func clear()  // Clears the queue
}

class MinPriorityQueue<DataType: Comparable & Hashable>: Queue
{
    private var queue: Array<DataType>
    private var contents: Set<DataType>

    public var size: Int { return self.queue.count }
    public var isEmpty: Bool { return self.queue.isEmpty }
    public init(initialState: Array<DataType> = []) {
        self.queue = initialState
        contents = Set(initialState)
    }

    @discardableResult
    public func add(_ item: DataType) -> Bool
    {
        if self.contents.contains(item) { return false }
        self.queue.append(item)
        self.contents.insert(item)
        self.heapifyUp(from: self.queue.count - 1)
        return true
    }

    @discardableResult
    public func remove() -> DataType? {
        return self.dequeue()
    }

    public func dequeue() -> DataType?
    {
        guard !self.queue.isEmpty else { return nil }
        let poppedItem = self.popAndHeapifyDown()
        self.contents.remove(poppedItem) 
        return poppedItem
    }

    public func peek() -> DataType? {
        return self.queue.first
    }

    public func contains(_ item: DataType) -> Bool {
        return self.contents.contains(item)
    }

    public func clear() {
        self.queue.removeAll()
        self.contents.removeAll()
    }


    // Restores the min heap order of the queue by moving an item
    // from the given index towards the beginning of the queue.
    private func heapifyUp(from index: Int)
    {
        var childIndex = index
        var parentIndex = index.parentIndex

        while parentIndex >= 0 && self.queue[parentIndex] > self.queue[childIndex] {
            self.queue.swapAt(childIndex, parentIndex)
            childIndex = parentIndex
            parentIndex = childIndex.parentIndex
        }
    }

    // Pops the first item in the queue, moves the rightmost element to the root
    // and restores the min heap order of the queue by moving the root item
    // towards the end of the queue. Returns the item popped.
    private func popAndHeapifyDown() -> DataType
    {
        let firstItem = self.queue[0]
        
        if self.queue.count == 1 {
            self.queue.removeLast()
            return firstItem
        }
        
        self.queue[0] = self.queue.removeLast()    
        self.heapifyDown()    
        return firstItem
    }

    // Restores the min heap order of the queue by moving
    // the root item towards the end of the queue.
    private func heapifyDown()
    {
        var parentIndex = 0
        var leftChildIndex: Int, rightChildIndex: Int, minChildIndex: Int  
        while true
        {
            leftChildIndex = parentIndex.leftChildIndex
            if leftChildIndex >= self.queue.count { break }
        
            rightChildIndex = parentIndex.rightChildIndex

            minChildIndex = (rightChildIndex < self.queue.count && 
                             self.queue[rightChildIndex] < self.queue[leftChildIndex]) ? 
            rightChildIndex : leftChildIndex
        
            if self.queue[parentIndex] > self.queue[minChildIndex] {
                self.queue.swapAt(minChildIndex, parentIndex)
                parentIndex = minChildIndex
            } else { break }
        }
    }
}

private extension Int {
    var leftChildIndex: Int { return (self * 2) + 1 }  
    var rightChildIndex: Int {  return (self * 2) + 2 }  
    var parentIndex: Int { return (self - 1) / 2 }
}

extension MinPriorityQueue: CustomStringConvertible {
    public var description: String {
        return self.queue.description
    }
}