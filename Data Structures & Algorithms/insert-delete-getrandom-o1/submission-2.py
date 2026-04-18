class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.size = 0
        self.array = []

    def insert(self, val: int) -> bool:
        if val not in self.num_map:
            self.num_map[val] = self.size
            self.array.append(val)
            self.size += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.num_map:
            return False
        
        remove_index = self.num_map[val]
        last_val = self.array[self.size - 1]

        self.array[remove_index] = last_val
        self.num_map[last_val] = remove_index

        self.array.pop()
        del self.num_map[val]
        self.size -= 1
        return True

    def getRandom(self) -> int:
        import random
        rand_num = random.randint(0, self.size - 1)
        return self.array[rand_num]