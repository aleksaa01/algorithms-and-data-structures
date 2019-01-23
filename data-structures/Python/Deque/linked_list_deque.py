from doubly_linked_list import DoublyLinkedList


class DLLDeque(object):

    def __init__(self, list_object=None):
        self.data = DoublyLinkedList()
        self.size = 0

        if list_object:
            self.data.build(list_object)
            self.size = len(list_object)

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        return self.data.head_value

    def last(self):
        return self.data.tail_value

    def appendfront(self, item):
        self.data.insert_front_value(item)
        self.size += 1

    def appendback(self, item):
        self.data.insert_end_value(item)
        self.size += 1

    def popfront(self):
        if self.size == 0:
            raise IndexError('Unable to popfront, Deque is empty.')

        self.size -= 1
        return self.data.pop_front_value()

    def popback(self):
        if self.size == 0:
            raise IndexError('Unable to popback, Deque is empty.')

        self.size -= 1
        return self.data.pop_back_value()


if __name__ == '__main__':
    import time
    
    def test1():
        dq = DLLDeque()
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
        dq = DLLDeque()
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
        dq = DLLDeque(long_list)
        while not dq.is_empty():
            dq.popfront()
        t2 = time.time()
        print('First part(build, popfront), time took:', t2 - t1)

        t1 = time.time()
        dq = DLLDeque(long_list)
        while not dq.is_empty():
            dq.popback()
        t2 = time.time()
        print('Second part(build, popback, time took:', t2 - t1)

        t1 = time.time()
        dq = DLLDeque()
        for i in range(1000000):
            dq.appendfront(i)
        for i in range(1000000):
            dq.popfront()
        t2 = time.time()
        print('Third part(appendfront, popfront), time took:', t2 - t1)

        t1 = time.time()
        dq = DLLDeque()
        for i in range(1000000):
            dq.appendback(i)
        for i in range(1000000):
            dq.popback()
        t2 = time.time()
        print('Fourth part(appendback, popback), time took:', t2 - t1)

        t1 = time.time()
        dq = DLLDeque()
        for i in range(1000000):
            dq.appendfront(i)
        for i in range(1000000):
            dq.popback()
        t2 = time.time()
        print('Fifth part(appendfront, popback), time took:', t2 - t1)

        t1 = time.time()
        dq = DLLDeque()
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
