class DynamicArray:
    current_len  = 0
    max_capacity = 0
    array = []

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.current_len = 0
        self.array = []


    def get(self, i: int) -> int:
        if self._is_index_valid(i):
            return self.array[i]

    def _is_index_valid(self, i:int) -> bool:
        return i >=0 and i < self.current_len

    def set(self, i: int, n: int) -> None:
        if self._is_index_valid(i):
            self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.current_len == self.max_capacity:
            self.resize()
        
        self.current_len += 1
        self.array.append(n)

    def popback(self) -> int:
        if self.current_len>0:
            self.current_len -= 1
            return self.array.pop(self.current_len)
        else:
            return None

    def resize(self) -> None:
        self.max_capacity *= 2

    def getSize(self) -> int:
        return self.current_len
    
    def getCapacity(self) -> int:
        return self.max_capacity
