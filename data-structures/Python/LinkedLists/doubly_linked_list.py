class Node(object):

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList(object):

    def __init__(self, list_object=None):
        self.header = Node(None)
        self.trailer = Node(None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        if isinstance(list_object, list):
            self.build(list_object)

    def build(self, list_object):
        for i in list_object:
            self.insert_end_node(Node(i))

    def insert_front_node(self, node):
        temp = self.header.next
        node.next, temp.prev = temp, node
        self.header.next, node.prev = node, self.header

    def insert_front_value(self, value):
        self.insert_front_node(Node(value))

    def insert_end_node(self, node):
        temp = self.trailer.prev
        node.prev, temp.next = temp, node
        self.trailer.prev, node.next = node, self.trailer

    def insert_end_value(self, value):
        self.insert_end_node(Node(value))

    def traverse_forward(self):
        cur = self.header.next
        while cur != self.trailer:
            yield cur.value
            cur = cur.next

    def traverse_backward(self):
        cur = self.trailer.prev
        while cur != self.header:
            yield cur.value
            cur = cur.prev

    def remove_node(self, node):
        prev_node = node.prev
        prev_node.next = node.next
        node.next.prev = prev_node
        del node

    def remove_value(self, value):
        cur = self.header.next
        while cur != self.trailer:
            if cur.value == value:
                self.remove_node(cur)
                break
            cur = cur.next

    def lfind(self, value):
        cur = self.header.next
        while cur != self.trailer:
            if cur.value == value:
                return cur
            cur = cur.next
        return None

    def rfind(self, value):
        cur = self.trailer.prev
        while cur != self.header:
            if cur.value == value:
                return cur
            cur = cur.prev

    def print_nodes(self, debug=False):
        if debug:
            print(self.head, self.tail, end=' ')
            print(self.head.value, self.tail.value, end=' ')
            print(self.head == self.tail)
        cur = self.header.next
        nodes = []
        while cur != self.trailer:
            nodes.append(cur.value)
            cur = cur.next
        return '[' + ', '.join(map(str, nodes)) + ']'


if __name__ == '__main__':
    def test1():
        dll = DoublyLinkedList([1, 2, 3, 4, 5])
        assert dll.print_nodes() == '[1, 2, 3, 4, 5]'
        dll.insert_front_value(6)
        dll.insert_end_value(100)
        assert dll.print_nodes() == '[6, 1, 2, 3, 4, 5, 100]'
        dll.remove_value(4)
        dll.remove_value(5)
        assert dll.print_nodes() == '[6, 1, 2, 3, 100]'
        assert [6, 1, 2, 3, 100] == [i for i in dll.traverse_forward()]
        assert [100, 3, 2, 1, 6] == [i for i in dll.traverse_backward()]
        print('Test 1 Done!')

    def test2():
        dll = DoublyLinkedList()
        dll.insert_front_value(5)
        assert dll.print_nodes() == '[5]'
        dll.remove_value(5)
        assert dll.print_nodes() == '[]'
        dll.insert_front_value(10)
        assert dll.print_nodes() == '[10]'
        dll.remove_value(10)
        dll.insert_end_value(8)
        assert dll.print_nodes() == '[8]'
        dll.insert_end_value(17)
        assert dll.print_nodes() == '[8, 17]'
        print('Test 2 Done!')

    test1()
    test2()
