class Node:

    left_child = None
    right_child = None

    def __init__(self, key):
        self.key = key

class BinarySearchTree:
    
    def __init__(self, root = None):
        self.root = root


    def insert(self, node):
        def insertNode(pointer, node):
            if pointer == None:
                return node
            if node.key < pointer.key:
                pointer.left_child = insertNode(pointer.left_child, node)
            else:
                pointer.right_child = insertNode(pointer.right_child, node)
            return pointer
        self.root = insertNode(self.root, node)

    def remove(self, val):
        def deleteNode(pointer, val):
            if pointer == None:
                return None
            if val < pointer.key:
                pointer.left_child = deleteNode(pointer.left_child, val)
            elif val > pointer.key:
                pointer.right_child = deleteNode(pointer.right_child, val)
            else:
                if pointer.right_child == None:
                    return pointer.left_child
                elif pointer.left_child == None:
                    return pointer.right_child
                minnode = pointer.right_child
                while minnode.left_child != None :
                    minnode = minnode.left_child
                pointer.key = minnode.key
                pointer.right_child = deleteNode(pointer.right_child, minnode.key)
            return pointer

        self.root = deleteNode(self.root, val)
        return Node(val)


    def search(self, val, node = None):
        n = self.root
        if node is not None:
            n = node
        def find(val, node):
            if node is None:
                return False
            if val < node.key:
                return find(val, node.left_child)
            elif val > node.key:
                return find(val, node.right_child)
            else:
                return True
        return find(val, n)

    def min(self):
        def findmin(node):
            if node is None:
                return None
            while(node.left_child != None):
                node = node.left_child
            return node.key
        return findmin(self.root)
    
    def max(self):
        def findmax(node):
            if node is None:
                return None
            while(node.right_child != None):
                node = node.right_child
            return node.key
        return findmax(self.root)
