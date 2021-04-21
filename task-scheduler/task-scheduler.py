class Solution:
    def leastInterval(self, tasks: List[str], cooldown_period: int) -> int:
      pq = []
      counts = Counter(tasks)
      for c in counts.values(): heappush(pq, -1 * c)
      idle_units = 0
      while pq:
        curr_list = []
        curr_list.append(-1 * heappop(pq) - 1)
        if curr_list[0] == 0:
          break
        for i in range(cooldown_period):
          if pq:
            curr_list.append(-1 * heappop(pq) - 1) 
          else:
            idle_units += 1
        # print(curr_list)
        for el in curr_list:
          if el > 0:
            heappush(pq, -1 * el)
            
      return len(tasks) + idle_units    
                