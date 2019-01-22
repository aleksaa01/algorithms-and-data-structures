class ArrayQueue(object):

    DEFAULT_SIZE = 10

    def __init__(self, list_object=None):
        if list_object:
            self.data = list_object
            self.front = len(list_object) - 1
            self.back = 0
            self.size = len(list_object)
            return

        self.data = [None] * self.DEFAULT_SIZE
        self.front = -1
        self.back = 0
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        return self.data[self.back]

    def enqueue(self, item):
        if self.size >= len(self.data):
            self.grow()

        self.front += 1
        self.front %= len(self.data)

        self.data[self.front] = item
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError('Unable to dequeue, Queue is empty.')
        elif self.size > self.DEFAULT_SIZE and self.size < len(self.data) // 2:
            self.shrink()

        item = self.data[self.back]
        self.data[self.back] = None
        self.size -= 1

        self.back += 1
        self.back %= len(self.data)
        return item

    def grow(self):
        front = self.front
        back = self.back
        queue_len = len(self.data)

        if front < (queue_len - 1):
            self.data = self.data[back:] + self.data[:front+1] + [None] * (queue_len // 2)
        else:
            self.data = self.data[back:front+1] + [None] * (queue_len // 2)

        self.front = self.size - 1
        self.back = 0

    def shrink(self):
        front = self.front
        back = self.back
        queue_size = self.size

        if front < (queue_size - 1):
            self.data = self.data[back:queue_size] + self.data[:front+1]
        else:
            self.data = self.data[back:front+1]

        self.front = self.size - 1
        self.back = 0


if __name__ == '__main__':
    import time

    def test1():
        q = ArrayQueue()
        for i in range(9):
            q.enqueue(i)
        assert q.peek() == 0
        assert q.is_empty() == False
        for i in range(9):
            assert q.dequeue() == i
        assert q.peek() == None
        assert q.is_empty() == True
        print('Test 1 is Done.')


    def test2():
        q = ArrayQueue()
        num_range = 120
        for i in range(num_range):
            q.enqueue(i)
            assert q.peek() == 0
            assert q.is_empty() == False
            assert len(q) == (i + 1)
        for i in range(num_range):
            assert q.peek() == i
            assert q.is_empty() == False
            assert len(q) == (num_range - i)
            assert q.dequeue() == i
        assert q.peek() == None
        assert q.is_empty() == True
        print('Test 2 is Done.')

    def test3():
        print('Start test 3(processing 1.000.000 items in 2 ways)...')
        t1 = time.time()
        q = ArrayQueue([i for i in range(1000000)])
        while not q.is_empty():
            q.dequeue()
        t2 = time.time()
        print('First part, time took:', t2 - t1)

        t1 = time.time()
        q = ArrayQueue()
        for i in range(1000000):
            q.enqueue(i)
        for i in range(1000000):
            q.dequeue()
        t2 = time.time()
        print('Second part, time took:', t2 - t1)
        print('Test 3 is Done.')


    test1()
    test2()
    test3()
