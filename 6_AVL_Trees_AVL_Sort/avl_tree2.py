class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.root = self._insert(value, self.root)

    def _insert(self, value, node):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left_child = self._insert(value, node.left_child)
        else:
            node.right_child = self._insert(value, node.right_child)

        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))

        balance = self.get_balance(node)

        if balance > 1 and value < node.left_child.value:
            return self.rotate_right(node)

        if balance < -1 and value > node.right_child.value:
            return self.rotate_left(node)

        if balance > 1 and value > node.left_child.value:
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)

        if balance < -1 and value < node.right_child.value:
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)

        return node

    def get_height(self, node):
        if not node:
            return 0

        return node.height

    def get_balance(self, node):
        if not node:
            return 0

        return self.get_height(node.left_child) - self.get_height(node.right_child)

    def rotate_right(self, node):
        new_root = node.left_child
        node.left_child = new_root.right_child
        new_root.right_child = node
        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
        new_root.height = 1 + max(self.get_height(new_root.left_child), self.get_height(new_root.right_child))
        return new_root

    def rotate_left(self, node):
        new_root = node.right_child
        node.right_child = new_root.left_child
        new_root.left_child = node
        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
        new_root.height = 1 + max(self.get_height(new_root.left_child), self.get_height(new_root.right_child))
        return new_root

if __name__ == '__main__':
    avl_tree = AVLTree()
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    avl_tree.insert(40)
    avl_tree.insert(50)
    avl_tree.insert(25)

print(avl_tree)