from object import Object, Color
from exceptions import NoBinFoundException
from node import Node

def comp_1(node_1, node_2):
    return node_1.key > node_2.key


class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.size = 0

    #returns height of node
    def height(self, node):
        if node is None:
            return 0
        return node.height
    
    #computes balance factor of node
    def balancefactor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    #new height after every operation
    def new_height(self, p):
        p.height = 1 + max(self.height(p.left), self.height(p.right))

    #checks if the tree is balanced at node p or not
    def balanced(self, p):
        return abs(self.balancefactor(p)) <= 1

    #left rotates
    def rotate_left(self, z):
        y = z.right
        z.right = y.left
        if y.left is not None:
            y.left.parent = z
        y.parent = z.parent
        if z.parent is None:
            self.root = y
        elif z == z.parent.left:
            z.parent.left = y
        else:
            z.parent.right = y
        y.left = z
        z.parent = y

        self.new_height(z)
        self.new_height(y)

    #right rotates
    def rotate_right(self, z):
        y = z.left
        z.left = y.right
        if y.right is not None:
            y.right.parent = z
        y.parent = z.parent
        if z.parent is None:
            self.root = y
        elif z == z.parent.right:
            z.parent.right = y
        else:
            z.parent.left = y
        y.right = z
        z.parent = y

        self.new_height(z)
        self.new_height(y)

    #rebalancing according to balance factors
    def rebalance(self, node):
        while node is not None:
            self.new_height(node)
            balance = self.balancefactor(node)

            if balance > 1:
                if self.balancefactor(node.left) < 0:
                    self.rotate_left(node.left)
                self.rotate_right(node)

            elif balance < -1:
                if self.balancefactor(node.right) > 0:
                    self.rotate_right(node.right)
                self.rotate_left(node)

            node = node.parent

    #inserting a node on an AVL tree with key-value given
    def insert(self, key, value):
        new_node = Node(key, value)

        if self.root is None:
            self.root = new_node
            self.size += 1
            return
        else:
            current = self.root
            parent = None

            while current is not None:
                parent = current
                if new_node.key > current.key:
                    current = current.right
                else:
                    current = current.left

            if new_node.key > parent.key:
                parent.right = new_node
            else:
                parent.left = new_node

            new_node.parent = parent
            self.size += 1

            self.rebalance(new_node)

    #searches for the node with key
    def search(self, key):
        current = self.root
        while current is not None:
            if current.key == key:
                return current
            elif key > current.key:
                current = current.right
            else:
                current = current.left
        return None

    #deleting a node in an AVL tree with key
    def delete(self, key):
        node_to_delete = self.search(key)

        if node_to_delete is None:
            print(f"Node with key {key} not found")
            return False

        if node_to_delete.left is None and node_to_delete.right is None:
            if node_to_delete == self.root:
                self.root = None
            elif node_to_delete == node_to_delete.parent.left:
                node_to_delete.parent.left = None
            else:
                node_to_delete.parent.right = None
            self.rebalance(node_to_delete.parent)

        elif node_to_delete.left is None or node_to_delete.right is None:
            child = node_to_delete.left if node_to_delete.left else node_to_delete.right
            if node_to_delete == self.root:
                self.root = child
                child.parent = None
            else:
                if node_to_delete == node_to_delete.parent.left:
                    node_to_delete.parent.left = child
                else:
                    node_to_delete.parent.right = child
                child.parent = node_to_delete.parent
            self.rebalance(node_to_delete.parent)
        else:
            successor = self.minimum_in_subtree(node_to_delete.right)
            node_to_delete.key = successor.key
            node_to_delete.value = successor.value

            if successor.right:
                if successor == successor.parent.left:
                    successor.parent.left = successor.right
                else:
                    successor.parent.right = successor.right
                successor.right.parent = successor.parent
            else:
                if successor == successor.parent.left:
                    successor.parent.left = None
                else:
                    successor.parent.right = None

            self.rebalance(successor.parent)

        return True
        
    #returns node with minimum key in the subtree of node
    def minimum_in_subtree(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    #returns node with maximum key in the subtree of node
    def maximum_in_subtree(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    # In-order traversal to show bin_info
    def inorder(self, node):
        if node is None:
            return []

        left_subtree = self.inorder(node.left)
        curr = [node.key]
        right_subtree = self.inorder(node.right)

        return left_subtree + curr + right_subtree

    # Function to print all nodes in form of tuples
    def print_as_tuples(self):
        result = self.inorder(self.root)
        return result  

    # Finding successor of node with key 
    def successor(self, key):
        node = self.search(key)

        if node is None:
            return None

        if node.right:
            return self.minimum_in_subtree(node.right)

        successor = None
        while node.parent:
            if node == node.parent.left:
                successor = node.parent
                break
            node = node.parent

        return successor

    # Finding predessesor of node with key 
    def predecessor(self, key):
        node = self.search(key)

        if node is None:
            return None

        if node.left:
            return self.maximum_in_subtree(node.left)

        predecessor = None
        while node.parent:
            if node == node.parent.right:
                predecessor = node.parent
                break
            node = node.parent

        return predecessor

    # Finding successor when the key is not present in the tree
    def find_successor_in_absence(self, root, key):
        successor = None
        temp = root

        while temp:
            if temp.key >= key:

                successor = temp
                temp = temp.left
            else:

                temp = temp.right

        return successor



        