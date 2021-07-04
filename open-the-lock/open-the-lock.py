class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
      def genNbrs(curr):
        curr = list(curr)
        nbrs = []
        for i in range(4):
          temp = curr[i]
          curr[i] = (curr[i] + 1) % 10
          nbrs += [tuple(curr)]
          curr[i] = temp
          
          temp = curr[i]
          curr[i] = (curr[i] - 1) % 10
          nbrs += [tuple(curr)]
          curr[i] = temp
        return nbrs
      
      if '0000' in deadends: return -1
      
      t = tuple([int(c) for c in target])
      visited = set([tuple([int(c) for c in deadend]) for deadend in deadends])
      q = [((0, 0, 0, 0), 0)]
      while q:
        curr, depth = q.pop(0)
        if curr == t:
          return depth
        nbrs = genNbrs(curr)
        for nbr in nbrs:
          if nbr not in visited:
            visited.add(nbr)
            q += [(nbr, depth + 1)]
      return -1