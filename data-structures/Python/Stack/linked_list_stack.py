from singly_linked_list import SinglyLinkedList


class SLLStack:
    def __init__(self):
        self.size = 0
        self._data = SinglyLinkedList()

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        self.size += 1
        self._data.add_value(e)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        top = self._data.head.value
        self._data.delete_value(self._data.head.value)
        self.size -= 1
        return top

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data.head.value


if __name__ == '__main__':
    import time

    def test1():
        s = SLLStack()
        for i in range(10, -1, -1):
            s.push(i)
        for i in range(11):
            assert s.pop() == i

    def test2():
        s = SLLStack()
        t1 = time.perf_counter()
        for i in range(100000):
            s.push(i)
        t2 = time.perf_counter()
        print('Pushing 100.000 items took:', t2 - t1)

        t1 = time.perf_counter()
        for i in range(100000):
            s.pop()
        t2 = time.perf_counter()
        print('Popping 100.000 items took:', t2 - t1)

    test1()
    test2()
    print('All test done.')
