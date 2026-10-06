class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.data = [None] * capacity


    def get(self, i: int) -> int:
        return self.data[i]


    def set(self, i: int, n: int) -> None:
        self.data[i] = n


    def pushback(self, n: int) -> None:
        if self.length >= self.capacity:
            self.resize()
        self.data[self.length] = n
        self.length += 1


    def popback(self) -> int:
        self.length -= 1
        return self.data[self.length]
 

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_data = [0] * self.capacity
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity