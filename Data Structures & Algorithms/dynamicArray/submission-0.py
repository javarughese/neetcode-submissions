class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        if(i >= 0 and i < self.size):
            return self.arr[i]
        else:
            raise IndexError("Index out of Bounds")

    def set(self, i: int, n: int) -> None:
        if ( i >= 0 and i < self.size):
            self.arr[i] = n
        else: 
            raise IndexError("Index out of Bounds")

    def pushback(self, n: int) -> None:
        if(self.size == self.capacity):
            self.resize()
        self.arr[self.size] = n
        self.size += 1


    def popback(self) -> int:
        if (self.size == 0):
            return None
        num = self.get(self.size-1)
        self.arr[self.size-1] = 0
        self.size -= 1
        return num

    def resize(self) -> None:
        newCapacity = self.capacity * 2
        self.capacity = newCapacity
        new = [0]*self.capacity

        for i in range(self.size):
            new[i] = self.arr[i]
        self.arr = new

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
