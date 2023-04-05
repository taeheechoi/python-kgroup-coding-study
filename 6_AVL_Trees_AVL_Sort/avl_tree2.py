class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if not node:
                return Node(key)
            elif key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)

            node.height = 1 + max(self._height(node.left), self._height(node.right))
            balance = self._get_balance(node)

            # Left Left Case
            if balance > 1 and key < node.left.key:
                return self._right_rotate(node)

            # Right Right Case
            if balance < -1 and key > node.right.key:
                return self._left_rotate(node)

            # Left Right Case
            if balance > 1 and key > node.left.key:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

            # Right Left Case
            if balance < -1 and key < node.right.key:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

            return node

        self.root = _insert(self.root, key)

    def in_order_traversal(self):
        def _in_order_traversal(node, result):
            if node:
                _in_order_traversal(node.left, result)
                result.append(node.key)
                _in_order_traversal(node.right, result)

            return result

        return _in_order_traversal(self.root, [])

    def _height(self, node):
        if not node:
            return 0

        return node.height

    def _get_balance(self, node):
        if not node:
            return 0

        return self._height(node.left) - self._height(node.right)

    def _left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))

        return new_root

    def _right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))

        return new_root

def avl_sort(arr):
    tree = AVLTree()

    for elem in arr:
        tree.insert(elem)

    return tree.in_order_traversal()


arr = [5, 2, 7, 1, 9, 3, 8, 4, 6]
sorted_arr = avl_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
