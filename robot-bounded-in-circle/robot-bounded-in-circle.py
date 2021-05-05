def rangel(a):
    return range(len(a))

def getDir(curr, instr):
    """
    -> : (0, 1)

     | : (-1, 0)
    \ /

    <- : (0, -1)

    / \
     | : (1, 0)
    """
    if curr == (-1, 0):
        if instr == 'L':
            return (0, 1)
        elif instr == 'R':
            return (0, -1)
    if curr == (0, -1):
        if instr == 'L':
            return (-1, 0)
        elif instr == 'R':
            return (1, 0)
    if curr == (0, 1):
        if instr == 'L':
            return (1, 0)
        elif instr == 'R':
            return (-1, 0)
    if curr == (1, 0):
        if instr == 'L':
            return (0, -1)
        elif instr == 'R':
            return (0, 1)

def move(pos, cdir):
    return [pos[0] + cdir[0], pos[1] + cdir[1]]
    
class Solution:        
    def isRobotBounded(self, instructions: str) -> bool:
        currPos = [0, 0]
        currDir = (0, 1)
        for _ in range(4):
            for instr in instructions:
                # print(currPos, currDir, instr, end=' ')
                if instr == 'G':
                    currPos = move(currPos, currDir)
                    # currPos = [max(currPos[0], 0), max(currPos[1], 0)]
                else:
                    currDir = getDir(currDir, instr)
                # print(currPos, currDir)
            # print(currPos)
            if currPos == [0, 0]:
                return True
                
        return False