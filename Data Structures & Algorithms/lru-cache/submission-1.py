class LRUCache:
    def __init__(self, capacity: int):
        self.hash_map = {}
        self.capacity = capacity
        self.LRU = [] 
        

    def get(self, key: int) -> int:
        if key in self.hash_map:
            self.LRU.remove(key)
            self.LRU.insert(0, key)
            return self.hash_map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.LRU.remove(key)
            self.LRU.insert(0, key)
            self.hash_map[key] = value
        elif len(self.LRU) < self.capacity:
            self.LRU.insert(0, key) 
            self.hash_map[key] = value
        else:
            self.hash_map.pop(self.LRU[-1])
            self.LRU.pop()
            self.LRU.insert(0,key)
            self.hash_map[key] = value




        
