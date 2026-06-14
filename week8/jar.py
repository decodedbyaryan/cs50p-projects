class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("negatice value")
        if not isinstance(capacity, int):
            raise ValueError("Not int")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if n + self._size > self._capacity:
            raise ValueError("exceed the capacity") 
        self._size += n
        
    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("negative output")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self._size
    
if __name__ == "__main__":
    jar = Jar()
    jar.deposit(3)
    print(jar)
    print(jar.size)
    print(jar.capacity)