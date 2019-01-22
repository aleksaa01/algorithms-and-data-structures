from doubly_linked_list import DoublyLinkedList


class DLLQueue(object):

    def __init__(self, list_object=None):
        self.data = DoublyLinkedList()
        self.size = 0
        
        if list_object:
            self.data.build(list_object)

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        return self.data.tail_value

    def enqueue(self, item):
        self.data.insert_front_value(item)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError('Unable to dequeue, Queue is empty.')

        value = self.data.pop_back_value()
        self.size -= 1
        return value


if __name__ == '__main__':
    import time

    def test1():
        q = DLLQueue()
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
        q = DLLQueue()
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
        q = DLLQueue([i for i in range(1000000)])
        while not q.is_empty():
            q.dequeue()
        t2 = time.time()
        print('First part, time took:', t2 - t1)

        t1 = time.time()
        q = DLLQueue()
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
