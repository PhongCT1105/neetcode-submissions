class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.size = 0
        self.array = []

    def insert(self, val: int) -> bool:
        if val not in self.num_map: # Not present
            self.size += 1
            self.num_map[val] = self.size - 1
            self.array.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.num_map: # Not present
            return False
        else:
            remove_index = self.num_map[val]
            self.array[remove_index] = self.array[self.size-1]
            self.array.pop()
            del self.num_map[val]
            self.num_map[val] = remove_index
            self.size -= 1
            return True 

    def getRandom(self) -> int:
        import random
        rand_num = random.randint(0, self.size-1)
        return self.array[rand_num]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()