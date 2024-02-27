import 'dart:collection';

class Solution {
  int orangesRotting(List<List<int>> grid) {
    var q = Queue();
    var visited = <String>{};
    for (var x = 0; x < grid.length; x++) {
      for (var y = 0; y < grid[0].length; y++) {
        if (grid[x][y] == 2) {
          q.add([
            [x, y],
            0
          ]);
          visited.add('$x$y');
        } else if (grid[x][y] == 0) {
          visited.add('$x$y');
        }
      }
    }
    var maxLevel = 0;
    while (q.isNotEmpty) {
      var curr = q.removeFirst();
      var level = curr[1];
      maxLevel = level > maxLevel ? level : maxLevel;
      visited.add('${curr[0][0]}${curr[0][1]}');
      if (visited.length == grid.length * grid[0].length) {
        break;
      }
      for (var move in [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
      ]) {
        var cd = [curr[0][0] + move[0], curr[0][1] + move[1]];
        var cdStr = '${cd[0]}${cd[1]}';
        if (cd[0] >= 0 &&
            cd[0] < grid.length &&
            cd[1] >= 0 &&
            cd[1] < grid[0].length &&
            !visited.contains(cdStr)) {
          q.add([cd, level + 1]);
        }
      }
    }
    if (visited.length != grid.length * grid[0].length) {
      return -1;
    }
    return maxLevel;
  }
}