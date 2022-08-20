class MyHashSet:

    def __init__(self):
        self.data = [-1] * 1000001

    def add(self, key: int) -> None:
        self.data[key] = key

    def remove(self, key: int) -> None:
        self.data[key] = -1

    def contains(self, key: int) -> bool:
        return self.data[key] != -1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)