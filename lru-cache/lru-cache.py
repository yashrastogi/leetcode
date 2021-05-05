class LRUCache:

    def __init__(self, capacity: int):
        self.curr_rank = 0
        self.cache = {}
        self.recent = {}
        self.capacity = capacity
    
    def _set_rank(self, key):
        self.recent[key] = self.curr_rank
        self.curr_rank += 1

    def get(self, key: int) -> int:
        if key in self.cache:
            self._set_rank(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        exists = True if key in self.cache else False
        self.cache[key] = value
        self._set_rank(key)
        if not exists:
            if len(self.cache) > self.capacity:
                tupl = min(self.recent.items(), key=lambda x: x[1])
                self.recent.pop(tupl[0])
                self.cache.pop(tupl[0])
        
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)