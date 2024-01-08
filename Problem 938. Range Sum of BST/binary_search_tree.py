class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)

        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest
            # in the right subtree)
            root.key = self._min_value_node(root.right).key

            # Delete the inorder successor
            root.right = self._delete(root.right, root.key)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, root):
        result = []
        if root:
            result += self.inorder_traversal(root.left)
            result.append(root.key)
            result += self.inorder_traversal(root.right)
        return result

# Example Usage:
bst = BinarySearchTree()
elements = [5, 3, 7, 2, 4, 6, 8]

for element in elements:
    bst.insert(element)

print("Inorder Traversal:", bst.inorder_traversal(bst.root))

# Search and Delete examples
search_key = 4
search_result = bst.search(search_key)
if search_result:
    print(f"Element {search_key} found in the tree.")
    bst.delete(search_key)
    print(f"Element {search_key} deleted.")
else:
    print(f"Element {search_key} not found in the tree.")

print("Inorder Traversal after deletion:", bst.inorder_traversal(bst.root))
