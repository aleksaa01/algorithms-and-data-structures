"""
    Deque's front is at the beginning of the list and back at the end of the list.
    Unlike Queue, his front and back are swapped.
"""


class ArrayDeque(object):

    DEFAULT_SIZE = 10

    def __init__(self, list_object=None):
        if list_object:
            self.data = list_object
            self.front = 0
            self.back = len(list_object) - 1
            self.size = len(list_object)
            return

        self.data = [None] * self.DEFAULT_SIZE
        self.front = 0
        self.back = -1
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        return self.data[self.front]

    def last(self):
        return self.data[self.back]

    def appendfront(self, item):
        if self.size >= len(self.data):
            self.grow()

        self.front -= 1
        if self.front < 0:
            self.front %= len(self.data)

        self.data[self.front] = item
        self.size += 1

    def appendback(self, item):
        if self.size >= len(self.data):
            self.grow()

        self.back += 1
        if self.back >= len(self.data):
            self.back %= len(self.data)

        self.data[self.back] = item
        self.size += 1

    def popfront(self):
        if self.size == 0:
            raise IndexError('Unable to pop, Deque is empty.')
        elif self.size > self.DEFAULT_SIZE and self.size < len(self.data) // 2:
            self.shrink()

        item = self.data[self.front]
        self.data[self.front] = None
        self.size -= 1

        self.front += 1
        if self.front >= len(self.data):
            self.front %= len(self.data)
        return item

    def popback(self):
        if self.size == 0:
            raise IndexError('Unable to pop, Deque is empty.')
        elif self.size > self.DEFAULT_SIZE and self.size < len(self.data) // 2:
            self.shrink()

        item = self.data[self.back]
        self.data[self.back] = None
        self.size -= 1

        self.back -= 1
        if self.back < 0:
            self.back %= len(self.data)
        return item

    def grow(self):
        front = self.front
        back = self.back
        deque_size = self.size
        
        if front > back:
            self.data = self.data[front:] + self.data[:back + 1] + [None] * (deque_size // 2)
        else:
            self.data = self.data[front:back + 1] + [None] * (deque_size // 2)
        
        self.front = 0
        self.back = self.size - 1

    def shrink(self):
        front = self.front
        back = self.back
        deque_size = self.size

        if front > back:
            self.data = self.data[front:] + self.data[:back + 1]
        else:
            self.data = self.data[front:back + 1]

        self.front = 0
        self.back = self.size - 1


if __name__ == '__main__':
    # add test 2 up to 120 before time test !!! NOT WORKING !!!
    import time
    
    def test1():
        dq = ArrayDeque()
        for i in range(4):
            dq.appendfront(i)
        assert dq.first() == 3
        assert dq.last() == 0

        for i in range(4, 11):
            dq.appendback(i)
        assert dq.first() == 3
        assert dq.last() == 10

        for i in range(3, -1, -1):
            assert dq.popfront() == i
        assert dq.first() == 4
        assert dq.last() == 10

        for i in range(10, 3, -1):
            assert dq.popback() == i
        assert dq.first() == None
        assert dq.last() == None

        print('Test 1 is Done.')
    
    def test2():
        dq = ArrayDeque()
        num_range = 120
        for i in range(num_range):
            dq.appendback(i)
            assert dq.first() == 0
            assert dq.is_empty() == False
            assert len(dq) == (i + 1)
        for i in range(num_range):
            assert dq.first() == i
            assert dq.is_empty() == False
            assert len(dq) == (num_range - i)
            assert dq.popfront() == i
        assert dq.first() == None
        assert dq.is_empty() == True

        print('Test 2 is Done.')
    
    def test3():
        print('Start test 3(processing 1.000.000 items in 6 ways)...')
        long_list = [i for i in range(1000000)]

        t1 = time.time()
        dq = ArrayDeque(long_list)
        while not dq.is_empty():
            dq.popfront()
        t2 = time.time()
        print('First part(build, popfront), time took:', t2 - t1)

        t1 = time.time()
        dq = ArrayDeque(long_list)
        while not dq.is_empty():
            dq.popback()
        t2 = time.time()
        print('Second part(build, popback, time took:', t2 - t1)

        t1 = time.time()
        dq = ArrayDeque()
        for i in range(1000000):
            dq.appendfront(i)
        for i in range(1000000):
            dq.popfront()
        t2 = time.time()
        print('Third part(appendfront, popfront), time took:', t2 - t1)

        t1 = time.time()
        dq = ArrayDeque()
        for i in range(1000000):
            dq.appendback(i)
        for i in range(1000000):
            dq.popback()
        t2 = time.time()
        print('Fourth part(appendback, popback), time took:', t2 - t1)

        t1 = time.time()
        dq = ArrayDeque()
        for i in range(1000000):
            dq.appendfront(i)
        for i in range(1000000):
            dq.popback()
        t2 = time.time()
        print('Fifth part(appendfront, popback), time took:', t2 - t1)

        t1 = time.time()
        dq = ArrayDeque()
        for i in range(1000000):
            dq.appendback(i)
        for i in range(1000000):
            dq.popfront()
        t2 = time.time()
        print('Sixth part(appendback, popfront), time took:', t2 - t1)

        print('Test 3 is Done.')

    test1()
    test2()
    test3()
