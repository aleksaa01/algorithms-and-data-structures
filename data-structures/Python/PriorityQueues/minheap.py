class EmptyHeap(Exception):
    pass


class MinHeap(object):

    def __init__(self, list_object=None):
        if list_object:
            self.heapify(list_object)

        self.data = []

    def heapify(self, list_object):
        for i in list_object:
            self.push(i)

    def peek(self):
        if len(self.data) > 0:
            return self.data[0]
        return None

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, value):
        self.data.append(value)
        index = len(self.data) - 1
        self.sift_up(index, value)

    def pop(self):
        if len(self.data) == 0:
            raise EmptyHeap('Unable to pop, heap is empty.')
        max_value = self.data[0]
        self.delete()

        return max_value

    def delete(self):
        if len(self.data) == 0:
            raise EmptyHeap('Unable to delete, heap is empty.')
        elif len(self.data) == 1:
            self.data.pop()
            return

        last_value = self.data.pop()
        self.data[0] = last_value
        self.sift_down(0, last_value)

    def sift_up(self, index, value):
        while index > 0:
            parent = index // 2 - 1 if index % 2 == 0 else index // 2
            if self.data[parent] > value:
                self.data[index], self.data[parent] = self.data[parent], value
                index = parent
                continue
            break

    def sift_down(self, index, value):
        heap_size = len(self.data)
        while index < heap_size:
            first_index = index * 2 + 1
            first_value = None
            other_index = index * 2 + 2
            if first_index >= heap_size:
                break
            first_value = self.data[first_index]
            if other_index < heap_size and self.data[other_index] < first_value:
                first_index = other_index
                first_value = self.data[other_index]

            if first_value < value:
                self.data[index], self.data[first_index] = first_value, value
                index = first_index
                continue
            break


if __name__ == '__main__':
    import time

    def test1(vs_list=False):
        h = MinHeap()
        r = 10000 # grow time for heap is linear, but quadratic for list.
        t1 = time.time()
        for i in range(r, -1, -1):
            h.push(i)
        for i in range(r):
            assert h.pop() == i
        t2 = time.time()
        print('Time took:', t2 - t1)

        if not vs_list:
            return

        l = []
        t1 = time.time()
        for i in range(r, -1, -1):
            l.append(i)
        for i in range(r+1):
            assert min(l) == i
            l.remove(i)
        t2 = time.time()
        print('Time took:', t2 - t1)

    def test2():
        h = MinHeap()
        h.push(1)
        h.push(2)
        h.push(3)
        h.push(4)
        h.push(5)
        assert 1 == h.pop()
        assert 2 == h.pop()
        assert 3 == h.pop()
        h.push(100)
        h.push(5)
        h.push(99)
        assert 4 == h.pop()

    test1()
    print('All test done.')