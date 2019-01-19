class EmptyHeap(Exception):
    pass


class MaxHeap(object):

    def __init__(self, list_object=None):
        self.data = []
        if list_object:
            self.heapify(list_object)

    def heapify(self, list_object):
        index = len(list_object) // 2
        self.data = list_object[:]

        while index > -1:
            self.sift_down(index, list_object[index])
            index -= 1

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
            raise EmptyHeap("Unable to pop, heap is empty.")

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
            if value > self.data[parent]:
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
            if other_index < heap_size and self.data[other_index] > first_value:
                first_index = other_index
                first_value = self.data[other_index]

            if first_value > value:
                self.data[index], self.data[first_index] = first_value, value
                index = first_index
                continue
            break


if __name__ == '__main__':
    def test1():
        h = MaxHeap()
        h.push(1)
        h.push(2)
        h.push(3)
        h.push(4)
        h.push(5)
        assert 5 == h.pop()
        assert 4 == h.pop()
        assert 3 == h.pop()
        h.push(100)
        h.push(5)
        h.push(99)
        assert 100 == h.pop()

    def test2():
        h = MaxHeap()
        for i in range(10000, -1, -1):
            h.push(i)
        for i in range(10001):
            assert h.pop() == 10000 - i

    def test3():
        h = MaxHeap([1,2,3,4,5])
        for i in range(5, -1, -1):
            assert h.pop() == i
        h2 = MaxHeap([5,4,3,2,1])
        for i in range(5, -1, -1):
            assert h2.pop() == i

    test1()
    test2()
    print('All test done.')
