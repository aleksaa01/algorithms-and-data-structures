class ArrayStack(object):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return repr(self._data)

    def build(self, list_object):
        if not isinstance(list_object, list):
            return TypeError('build method only accepts object of type list.')

        for i in list_object:
            self._data.append(i)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[-1]


if __name__ == '__main__':
    import time

    def test1():
        s = ArrayStack()
        for i in range(10, -1, -1):
            s.push(i)
        for i in range(11):
            assert s.pop() == i

    def test2():
        s = ArrayStack()
        s.build([i for i in range(20)])
        for i in range(19, -1, -1):
            assert s.pop() == i

    def test3():
        s = ArrayStack()
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
    test3()
    print('All test done.')
