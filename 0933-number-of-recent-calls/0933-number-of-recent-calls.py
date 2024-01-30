class RecentCounter:

    def __init__(self):
        self.storage = []        

    def ping(self, t: int) -> int:
        self.storage.insert(0, t)
        low = max(1, t - 3000)
        counter = 0
        for i in range(min(len(self.storage), 3001)):
            if self.storage[i] >= low:
                counter += 1
        return counter

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)