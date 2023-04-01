# The time complexity of searching, inserting, and deleting nodes in a binary search tree is O(h), where h is the height of the tree 1. The space complexity of these operations is also O(h), since the maximum amount of space needed to store the recursion stack would be h.
# This implementation uses a class to define a node and a binary search tree. The insert() method is used to insert a new node into the tree. If the root node is empty, it creates a new node with the given value and sets it as the root. Otherwise, it calls the _insert() method to recursively traverse the tree and find the correct position for the new node based on its value. If the value already exists in the tree, it prints a message indicating that.

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if not current_node.left:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if not current_node.right:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)
        else:
            print("Value already exists in tree.")

if __name__ == '__main__':
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)