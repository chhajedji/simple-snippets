#!/usr/bin/env python3

# https://leetcode.com/problems/lru-cache

class LRUCache:

    def __init__(self, capacity: int):
        self.k = []
        self.cap = capacity
        self.pairs = {}

    def get(self, key: int) -> int:
        if key in self.pairs:
            self.k.remove(key)
            self.k.append(key)
            return self.pairs[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.pairs:
            if len(self.k) == self.cap:
                self.pairs.pop(self.k.pop(0))
                self.k.append(key)
                self.pairs[key] = value
            else:
                self.k.append(key)
                self.pairs[key] = value
        else:
            self.k.remove(key)
            self.k.append(key)
            self.pairs[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
