class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def _reset_rank(self, key, put=False):
        if key in self.cache:
            self.cache.move_to_end(key, last=False)
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self._reset_rank(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self._reset_rank(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem()
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)