class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 0
        self.left = None
        self.right = None
        self.parent = None
    
        