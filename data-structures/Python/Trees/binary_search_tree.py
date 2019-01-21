class Node(object):

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_node(data, self.root)

    def _insert_node(self, data, node):
        if data <= node.data:
            if node.left_child:
                self._insert_node(data, node.left_child)
            else:
                node.left_child = Node(data)
                node.left_child.parent = node
        else:
            if node.right_child:
                self._insert_node(data, node.right_child)
            else:
                node.right_child = Node(data)
                node.right_child.parent = node

    def min_value(self):
        if not self.root:
            raise ValueError('Tree is empty.')
        return self._min_value(self.root)

    def _min_value(self, node):
        if node.left_child:
            return self._min_value(node.left_child)
        return node.data

    def _min_node(self, node):
        if node.left_child:
            return self._min_node(node.left_child)
        return node

    def max_value(self):
        if not self.root:
            raise ValueError('Tree is empty.')
        return self._max_value(self.root)

    def _max_value(self, node):
        if node.right_child:
            return self._max_value(node.right_child)
        return node.data

    def _max_node(self, node):
        if node.right_child:
            return self._max_node(node.right_child)
        return node

    def traverse(self, method='in'):
        if not self.root:
            return iter(())
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

    def remove(self, data):
        if not self.root:
            raise ValueError('Tree is empty.')
        self._delete_value(data)

    def _delete_value(self, data):
        node = self.find(data, self.root)
        if node is False:
            raise ValueError('No node with value {}'.format(data))
        self._delete_node(node)

    def find(self, value, node):
        if node is None:
            return False
        if node.data > value:
            return self.find(value, node.left_child)
        elif node.data < value:
            return self.find(value, node.right_child)
        return node

    def _delete_node(self, node):
        parent_node = node.parent
        num_child = self._num_children(node)

        if num_child == 0:
            # If there is no parent then this is root node
            if not parent_node:
                self.root = None
            elif parent_node.left_child == node:
                parent_node.left_child = None
            elif parent_node.right_child == node:
                parent_node.right_child = None
        elif num_child == 1:
            if node.left_child:
                child = node.left_child
            else:
                child = node.right_child

            if not parent_node:
                self.root = child
            elif parent_node.left_child == node:
                parent_node.left_child = child
            else:
                parent_node.right_child = child
            child.parent = parent_node

        else:
            successor = self._max_node(node.left_child)
            node.data = successor.data
            self._delete_node(successor)

    def _num_children(self, node):
        num_children = 0
        if node.left_child:
            num_children += 1
        if node.right_child:
            num_children += 1
        return num_children


if __name__ == '__main__':
    # test
    print('Creating Binary Search Tree...')
    bst = BinarySearchTree()
    print('Done.')

    print('Inserting values...')
    bst.insert(40)
    bst.insert(10)
    bst.insert(30)
    bst.insert(60)
    bst.insert(50)
    bst.insert(5)
    bst.insert(70)
    print('Done.\n')

    print('min: ', bst.min_value())
    print('max: ', bst.max_value())

    print('\nTraversing In-order...')
    [print(i, end=" ") for i in bst.traverse()]
    print('Traversing Pre-order')
    [print(i, end=" ") for i in bst.traverse(method='pre')]
    print('Traversing Post-order')
    [print(i, end=" ") for i in bst.traverse(method='post')]

    print()

    values_to_remove = [i for i in bst.traverse()]
    for i in values_to_remove:
        print('Removing value: ', i)
        bst.remove(i)
        print('Traversing Pre-order...')
        [print(i, end=" ") for i in bst.traverse(method='pre')]