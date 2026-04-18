class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.size = 0
        self.array = [] 

    def insert(self, val: int) -> bool:
        if val not in self.hash_map:
            self.array.append(val)
            self.hash_map[val] = self.size
            self.size += 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hash_map:
            remove_index = self.hash_map[val]
            replace_index = self.size - 1
            replace_value = self.array[replace_index]
            self.array[remove_index] = replace_value
            self.hash_map[replace_value] = remove_index
            self.array.pop()
            del self.hash_map[val]
            self.size -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        import random
        rand_index = random.randint(0, self.size - 1)
        return self.array[rand_index]