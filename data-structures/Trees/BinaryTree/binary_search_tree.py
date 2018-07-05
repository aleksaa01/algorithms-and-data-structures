class Node(object):

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self._values = []

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data <= node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data)
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data)

    def min_value(self):
        if not self.root:
            raise ValueError('Tree is empty.')
        return self._min_value(self.root)

    def _min_value(self, node):
        if node.left_child:
            return self._min_value(node.left_child)
        return node.data

    def max_value(self):
        if not self.root:
            raise ValueError('Tree is empty.')
        return self._max_value(self.root)

    def _max_value(self, node):
        if node.right_child:
            return self._max_value(node.right_child)
        return node.data

    def traverse(self, type='in'):
        if not self.root:
            raise ValueError('Tree is empty.')
        self._values.clear()
        if type == 'in':
            self._traverse_inorder(self.root)
        elif type == 'pre':
            self._traverse_preorder(self.root)
        elif type == 'post':
            self._traverse_postorder(self.root)
        else:
            raise ValueError('type must be either "in", "pre" or "post".')
        return self._values

    def _traverse_inorder(self, node):
        if node.left_child:
            self._traverse_inorder(node.left_child)
        self._values.append(node.data)
        if node.right_child:
            self._traverse_inorder(node.right_child)

    def _traverse_preorder(self, node):
        self._values.append(node.data)
        if node.left_child:
            self._traverse_inorder(node.left_child)
        if node.right_child:
            self._traverse_inorder(node.right_child)

    def _traverse_postorder(self, node):
        if node.left_child:
            self._traverse_inorder(node.left_child)
        if node.right_child:
            self._traverse_inorder(node.right_child)
        self._values.append(node.data)

if __name__ == '__main__':
    # test
    bst = BinarySearchTree()
    bst.insert(40)
    bst.insert(10)
    bst.insert(5)
    bst.insert(30)
    bst.insert(60)
    bst.insert(50)
    bst.insert(70)
    print('min: ', bst.min_value())
    print('max: ', bst.max_value())
    print(bst.traverse())
    print(bst.traverse(type='pre'))
    print(bst.traverse(type='post'))
