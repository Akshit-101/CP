#  LFU Cache

from collections import defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}  # key -> (value, frequency)
        self.freq_to_keys = defaultdict(dict)  # frequency -> {key: True}

    def _update(self, key):
        value, freq = self.key_to_val_freq[key]
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq] and self.min_freq == freq:
            self.min_freq += 1
        freq += 1
        self.key_to_val_freq[key] = (value, freq)
        self.freq_to_keys[freq][key] = True

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        self._update(key)
        return self.key_to_val_freq[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_val_freq:
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self._update(key)
        else:
            if len(self.key_to_val_freq) >= self.capacity:
                lfu_key = next(iter(self.freq_to_keys[self.min_freq]))
                del self.key_to_val_freq[lfu_key]
                del self.freq_to_keys[self.min_freq][lfu_key]
            self.key_to_val_freq[key] = (value, 1)
            self.freq_to_keys[1][key] = True
            self.min_freq = 1

lfu = LFUCache(2)
lfu.put(1, 1)        # Add key=1 with value=1
lfu.put(2, 2)        # Add key=2 with value=2
print(lfu.get(1))    # Output: 1 (key=1 is accessed, increasing its frequency)
lfu.put(3, 3)        # Add key=3, key=2 is least frequently used, remove it
print(lfu.get(2))    # Output: -1 (key=2 was removed)
print(lfu.get(3))    # Output: 3 (key=3 is accessed)