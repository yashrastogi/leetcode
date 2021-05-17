/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * interface Robot {
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     public boolean move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     public void turnLeft();
 *     public void turnRight();
 *
 *     // Clean the current cell.
 *     public void clean();
 * }
 */

class Solution {
    int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    
    public void cleanRoom(Robot robot) {
        var visited = new HashSet<Pair<Integer, Integer>>();
        cleanDFS(robot, 0, 0, 0, visited);
    }
    
    public void cleanDFS(Robot r, int row, int col, int dirIdx, Set<Pair<Integer, Integer>> visited) {
        visited.add(new Pair<>(row, col));
        r.clean();
        for(int i=0; i<4; i++) {
            var newDirection = directions[(i + dirIdx) % 4];
            int rowx = row + newDirection[0];
            int colx = col + newDirection[1];
            if (!visited.contains(new Pair<>(rowx, colx)) && r.move()) {
                cleanDFS(r, rowx, colx, (i + dirIdx) % 4, visited);
                goBack(r);
            }
            r.turnRight();
        }
    }
    
    public void goBack(Robot r) {
        r.turnLeft();
        r.turnLeft();
        r.move();
        r.turnRight();
        r.turnRight();
    }
    
    public void print(Object o) {
        System.out.println(o);
    }
}
