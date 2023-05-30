'''creates a simple cookie jar'''
class Jar:

    def __init__(self, capacity=12, cookies = [], size=int()):

        self.capacity = capacity
        self.cookies = cookies
        self.size = size

    def __str__(self):

        cookiestr = str()
        for x in self.cookies:
            cookiestr += '🍪'

        return cookiestr

    def deposit(self, n):

        for x in range(n):
            self.cookies.append('🍪')

        self.size = len(self.cookies)

        if self.size > self.capacity:

            raise ValueError('Only 12 🍪s fit')

        else:
            return (self.cookies, self.size)


    def withdraw(self, n):

        if len(self.cookies) <= 0:
            raise ValueError('No 🍪 left')

        else:

            for _ in range(n):
                self.cookies.remove('🍪')
        self.size = len(self.cookies)

        return (self.cookies, self.size)

    @property
    def capacity(self):
       return self._capacity
    @capacity.setter
    def capacity(self,capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size
