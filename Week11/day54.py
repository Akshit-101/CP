# Problem Statement: “Design a data structure that follows the constraints of Least Recently Used (LRU) cache”.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hash map to store keys and their corresponding nodes
        self.head = Node(-1, -1)  # Dummy head node
        self.tail = Node(-1, -1)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: Node):
        # Adds a node right after the head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node):
        # Removes an existing node from the linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        # Retrieves a value from the cache
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)  # Moved the accessed node to the front
            self._add_node(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        # Inserts a value into the cache
        if key in self.cache:
            # Remove the old node
            self._remove_node(self.cache[key])
            del self.cache[key]

        # Adding the new node to the cache
        new_node = Node(key, value)
        self._add_node(new_node)
        self.cache[key] = new_node

        # If capacity is exceeded, removing the least recently used node
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self._remove_node(lru_node)
            del self.cache[lru_node.key]


# Initialize cache with capacity of 2
cache = LRUCache(2)

cache.put(1, 1)   # Cache is {1=1}
cache.put(2, 2)   # Cache is {1=1, 2=2}
print(cache.get(1))  # Expected output: 1, Cache is now {2=2, 1=1}