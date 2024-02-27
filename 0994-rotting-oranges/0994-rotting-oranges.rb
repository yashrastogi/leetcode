def oranges_rotting(grid)
    queue = []
    visited = Set.new

    grid.each_with_index do |row, x|
      row.each_with_index do |cell, y|
        if cell == 2
          queue.push([x, y, 0])
          visited.add([x, y])
        elsif cell == 0
          visited.add([x, y])
        end
      end
    end

    max_level = 0
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    until queue.empty?
      current = queue.shift
      level = current[2]
      max_level = [level, max_level].max
      visited.add([current[0], current[1]])

      break if visited.size == grid.size * grid[0].size

      directions.each do |move|
        new_x = current[0] + move[0]
        new_y = current[1] + move[1]

        if new_x >= 0 && new_x < grid.size && new_y >= 0 && new_y < grid[0].size && !visited.include?([new_x, new_y])
          queue.push([new_x, new_y, level + 1])
        end
      end
    end

    return -1 if visited.size != grid.size * grid[0].size

    max_level
  end