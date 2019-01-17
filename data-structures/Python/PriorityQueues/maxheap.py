class EmptyHeap(Exception):
    pass


class MaxHeap(object):

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
            raise EmptyHeap("Unable to pop, heap is empty.")

        max_value = self.data[0]
        self.delete()

        return max_value
    
    def delete(self):
        if len(self.data) == 0:
            raise EmptyHeap("Unable to delete, heap is empty.")

        last_value = self.data.pop()
        self.data[0] = last_value
        self.sift_down(0, last_value)

    def sift_up(self, index, value):
        while index > 0:
            parent = index // 2 - 1 if index % 2 == 0 else index // 2
            if value > self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
                continue
            break

    def sift_down(self, index, value):
        heap_len = len(self.data) - 1
        while index < heap_len:
            lchild = index * 2 + 1
            if lchild <= heap_len and self.data[lchild] > value:
                self.data[index], self.data[lchild] = self.data[lchild], self.data[index]
                index = lchild
                continue
            rchild = index * 2 + 2
            if rchild <= heap_len and self.data[rchild] > value:
                self.data[index], self.data[rchild] = self.data[rchild], self.data[index]
                index = rchild
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

    test1()
