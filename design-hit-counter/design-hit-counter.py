class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits_dict = {}
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hits_dict[timestamp] = self.hits_dict.setdefault(timestamp, 0) + 1
        if len(self.hits_dict) == 301:
            self.hits_dict.pop(min(self.hits_dict.keys()))
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        ret_sum = 0
        for i in range(timestamp-299, timestamp+1):
            if i in self.hits_dict:
                ret_sum += self.hits_dict[i]
        return ret_sum
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)