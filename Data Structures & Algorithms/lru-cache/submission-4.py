class LRUCache:

    def __init__(self, capacity: int):
        self.cache = [-1 for i in range(1000)]
        self.capacity = capacity
        self.track = []

    def get(self, key: int) -> int:
        for i in self.track:
            if i == key:
                self.track.remove(key)
                self.track.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        flag = True
        self.cache[key] = value
        #Check if the key is already in the cache and replace it as most recent
        print(" ==== START CYCLE ====")
        for i in self.track:
            print(i)
            if i == key:
                self.track.remove(key)
                self.track.append(key)
                flag = False
        # If we track more than allowed, remove the least used and reset it to -1
        if len(self.track)==self.capacity and flag:
            popped = self.track.pop(0)
            self.cache[popped] = -1
        if flag:
            self.track.append(key)
        print(self.capacity, self.track, self.cache[0:10])
