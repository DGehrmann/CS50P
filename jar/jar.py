class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if (self.size + n) > (self.capacity):
            raise ValueError("Not enough capacity available")
        self.size = self.size + n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Not enough cookies in jar")
        self.size = self.size - n

    #Getter
    @property
    def capacity(self):
        return self._capacity

    #Setter
    @capacity.setter
    def capacity(self,capacity):
        if type(capacity) != int or capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size