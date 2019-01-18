class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList(object):

    def __init__(self, list_object=None):
        self.head = None

        if isinstance(list_object, list):
            self.build(list_object)

    def build(self, list_object):
        for i in range(len(list_object) - 1, -1, -1):
            self.add_node(Node(list_object[i]))

    def add_node(self, node):
        old_head = self.head
        self.head = node
        self.head.next = old_head

    def add_value(self, value):
        self.add_node(Node(value))

    def delete_node(self, node):
        dummy_head = Node(0)
        dummy_head.next = self.head
        cur = dummy_head
        while cur.next:
            if cur.next == node:
                cur.next = cur.next.next
                break
            cur = cur.next
        self.head = dummy_head.next

    def delete_value(self, value):
        dummy_head = Node(0)
        dummy_head.next = self.head
        cur = dummy_head
        while cur.next:
            if cur.next.value == value:
                cur.next = cur.next.next
                break
            cur = cur.next
        self.head = dummy_head.next

    def find(self, value):
        cur = self.head
        while cur:
            if cur.value == value:
                return cur
            cur = cur.next
        return None

    def traverse(self):
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next
