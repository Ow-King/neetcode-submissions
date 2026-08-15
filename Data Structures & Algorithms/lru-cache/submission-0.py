class LRUCache:

    def __init__(self, capacity: int):
        self.values = OrderedDict()
        self.cap = capacity
        

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        self.values.move_to_end(key)
        return self.values[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values.move_to_end(key)
        self.values[key] = value

        if len(self.values) > self.cap:
            self.values.popitem(last = False)

        
