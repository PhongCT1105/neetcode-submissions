class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * self.capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length >= self.getCapacity():
            self.resize()
        
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            return_pop = self.arr[self.length - 1]
            self.arr[self.length - 1] = None
            self.length -= 1
        return return_pop


    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [None] * self.capacity

        for i in range (self.getSize()):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity