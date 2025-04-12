class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder_traversal(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        return self._inorder(node.left) + [node.key] + self._inorder(node.right) if node else []

    def preorder_traversal(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        return [node.key] + self._preorder(node.left) + self._preorder(node.right) if node else []

    def postorder_traversal(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        return self._postorder(node.left) + self._postorder(node.right) + [node.key] if node else []

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node to be deleted found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            node.key = self._min_value(node.right).key
            node.right = self._delete(node.right, node.key)
        return node

    def _min_value(self, node):
        # Traverse to the leftmost node to find the minimum value
        current = node
        while current.left:
            current = current.left
        return current

    def max_value(self):
        return self._max_value(self.root)

    def _max_value(self, node):
        current = node
        while current.right:
            current = current.right
        return current.key

    def min_value(self):
        return self._min_value(self.root).key if self.root else None

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if not node:
            return -1
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1

    def depth(self, key):
        return self._depth(self.root, key, 0)

    def _depth(self, node, key, current_depth):
        if not node:
            return -1
        if node.key == key:
            return current_depth
        elif key < node.key:
            return self._depth(node.left, key, current_depth + 1)
        else:
            return self._depth(node.right, key, current_depth + 1)

    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, node):
        if not node:
            return True
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return abs(left_height - right_height) <= 1 and self._is_balanced(node.left) and self._is_balanced(node.right)