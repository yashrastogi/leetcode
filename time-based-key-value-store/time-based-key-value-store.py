class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.di = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.di.setdefault(key, [])
        self.di[key] += [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.di: return ""
        search = self.di[key]
        bs_idx = bisect_left(search, (timestamp, ))
        if bs_idx == 0 and search[bs_idx][0] > timestamp:
            return ""
        if bs_idx < len(search) and search[bs_idx][0] == timestamp:
            return search[bs_idx][1]    
        return search[bs_idx-1][1]
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)