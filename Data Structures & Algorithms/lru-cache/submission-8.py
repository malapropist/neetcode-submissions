class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.time_to_key = {}
        self.key_to_time = {}
        self.time = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        old_time = self.key_to_time[key]
        del self.time_to_key[old_time]

        self.time_to_key[self.time] = key
        self.key_to_time[key] = self.time
        self.time += 1

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_time = self.key_to_time[key]
            del self.time_to_key[old_time]
        elif len(self.cache) == self.capacity:
            oldest = min(self.time_to_key)
            lru_key = self.time_to_key.pop(oldest)
            del self.cache[lru_key]
            del self.key_to_time[lru_key]

        self.cache[key] = value
        self.time_to_key[self.time] = key
        self.key_to_time[key] = self.time
        self.time += 1