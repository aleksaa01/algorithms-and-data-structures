class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return repr(self._data)

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
    def test1():
        s = ArrayStack()
        for i in range(10, -1, -1):
            s.push(i)
        for i in range(11):
            assert s.pop() == i

    test1()
    print('All test done.')
