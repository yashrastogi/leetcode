class StockSpanner {
    var stack = [(Int, Int)]()
    
    func next(_ price: Int) -> Int {        
        var count = 1
        while let last = stack.last, last.0 <= price {
            count += last.1
            stack.removeLast()
        }
        stack.append((price, count))
        return count
    }
}