class Solution {
    func orangesRotting(_ grid: [[Int]]) -> Int {
        var queue = [[Int]]()
        var visited = Set<[Int]>()
        
        for x in 0..<grid.count {
            for y in 0..<grid[0].count {
                if grid[x][y] == 2 {
                    queue.append([x, y, 0])
                    visited.insert([x, y])
                } else if grid[x][y] == 0 {
                    visited.insert([x, y])
                }
            }
        }
        
        var maxLevel = 0
        let directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        while !queue.isEmpty {
            let current = queue.removeFirst()
            let level = current[2]
            maxLevel = max(level, maxLevel)
            visited.insert([current[0], current[1]])
            
            if visited.count == grid.count * grid[0].count {
                break
            }
            
            for move in directions {
                let newX = current[0] + move[0]
                let newY = current[1] + move[1]
                
                if newX >= 0 && newX < grid.count && newY >= 0 && newY < grid[0].count && !visited.contains([newX, newY]) {
                    queue.append([newX, newY, level + 1])
                }
            }
        }
        
        if visited.count != grid.count * grid[0].count {
            return -1
        }
        
        return maxLevel
    }
}