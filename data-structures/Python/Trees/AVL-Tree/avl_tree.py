class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.height = 0
        self.left_child = None
        self.right_child = None


class AVLTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            new_node = self._insert(self.root, data)
            self._walk_up(new_node)

    def _insert(self, node, data):
        if data <= node.data:
            if not node.left_child:
                node.left_child = Node(data)
                node.left_child.parent = node
                return node.left_child
            return self._insert(node.left_child, data)
        else:
            if not node.right_child:
                node.right_child = Node(data)
                node.right_child.parent = node
                return node.right_child
            return self._insert(node.right_child, data)

    def _walk_up(self, node):
        if not node:
            return
        else:
            self._check_node(node)
            return self._walk_up(node.parent)

    def _check_node(self, node):
        left_height = -1
        right_height = -1
        if node.left_child:
            left_height = node.left_child.height
        if node.right_child:
            right_height = node.right_child.height
        if abs(left_height - right_height) > 1:
            if left_height < right_height:
                self.left_rotate(node, node.right_child)
            else:
                self.right_rotate(node, node.left_child)
        else:
            node.height = max(left_height, right_height) + 1

    def left_rotate(self, node, child_node):
        if child_node.left_child:
            node.right_child = child_node.left_child
            node.right_child.parent = node
        else:
            node.right_child = None

        if node != self.root:
            child_node.parent = node.parent
            node.parent.right_child = child_node
        else:
            child_node.parent = None
            self.root = child_node

        child_node.left_child = node
        node.parent = child_node

        node.height -= 1

    def right_rotate(self, node, child_node):
        if child_node.right_child:
            node.left_child = child_node.right_child
            node.left_child.parent = node
        else:
            node.left_child = None

        if node != self.root:
            child_node.parent = node.parent
            node.parent.left_child = child_node
        else:
            child_node.parent = None
            self.root = child_node

        child_node.right_child = node
        node.parent = child_node

        node.height -= 1

    def traverse(self, method='in'):
        if not self.root:
            raise ValueError('Tree is empty.')
        if method == 'in':
            return self._traverse_inorder(self.root)
        elif method == 'pre':
            return self._traverse_preorder(self.root)
        elif method == 'post':
            return self._traverse_postorder(self.root)
        else:
            raise ValueError('method must be either "in", "pre" or "post".')

    # left subtree -> root -> right subtree
    def _traverse_inorder(self, node):
        if node.left_child:
            yield from self._traverse_inorder(node.left_child)
        yield node.data
        if node.right_child:
            yield from self._traverse_inorder(node.right_child)

    # root -> left subtree -> right subtree
    def _traverse_preorder(self, node):
        yield node.data
        if node.left_child:
            yield from self._traverse_inorder(node.left_child)
        if node.right_child:
            yield from self._traverse_inorder(node.right_child)

    # left subtree -> right subtree -> root
    def _traverse_postorder(self, node):
        if node.left_child:
            yield from self._traverse_inorder(node.left_child)
        if node.right_child:
            yield from self._traverse_inorder(node.right_child)
        yield node.data


if __name__ == '__main__':
    def test1():
        avl = AVLTree()
        avl.insert(1)
        avl.insert(2)
        avl.insert(3)
        assert [2, 1, 3] == [i for i in avl.traverse(method='pre')]

    def test2():
        avl = AVLTree()
        avl.insert(3)
        avl.insert(2)
        avl.insert(1)
        assert [2, 1, 3] == [i for i in avl.traverse(method='pre')]

    def test3():
        avl = AVLTree()
        avl.insert(10)
        avl.insert(5)
        avl.insert(20)
        avl.insert(1)
        avl.insert(7)
        avl.insert(15)
        avl.insert(25)
        avl.insert(30)
        avl.insert(22)
        avl.insert(35)
        assert [10, 1, 5, 7, 15, 20, 22, 25, 30, 35] == ([i for i in avl.traverse(method='pre')])

    test1()
    test2()
    test3()
