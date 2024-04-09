class HashTableSet:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def add(self, key):
        index = self._hash_function(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def remove(self, key):
        index = self._hash_function(key)
        if key in self.table[index]:
            self.table[index].remove(key)

    def contains(self, key):
        index = self._hash_function(key)
        return key in self.table[index]


# Example usage:
hash_set = HashTableSet()
hash_set.add("apple")
hash_set.add("banana")
hash_set.add("orange")

print(hash_set.contains("apple"))  # True
print(hash_set.contains("grape"))  # False

hash_set.remove("banana")
print(hash_set.contains("banana"))  # False
