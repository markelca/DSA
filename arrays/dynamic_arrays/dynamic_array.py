# url: https://neetcode.io/problems/dynamicArray
class DynamicArray:

    def __init__(self, capacity: int):
        assert capacity > 0, "capacity must be greater than 0"
        self.array = [0] * capacity
        self.capacity = capacity
        self.size = 0



    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        i = self.size - 1
        n = self.array[i]

        self.array[i] = 0
        self.size -= 1

        return n
 

    def resize(self) -> None:
        self.array += [0] * self.size
        self.capacity *= 2


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity


a = DynamicArray(5)
a.pushback(1)
a.pushback(2)
a.pushback(3)
a.pushback(4)
a.pushback(5)
a.pushback(6)
print(a.popback())
print(a.array)
print(a.getSize())
print(a.getCapacity())
