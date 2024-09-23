from avl import AVLTree
from object import Object, Color

class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id = bin_id
        self.capacity = capacity
        self.objects_AVLTreeinside = AVLTree()  # AVLTREE of objects_AVLTree in the bin

    def add_object_for_bin(self, obj):
        if obj.size <= self.capacity:
            self.objects_AVLTreeinside.insert(obj.object_id, obj)
            self.capacity -= obj.size
        else:
            raise NoBinFoundException

    def remove_object_from_bin(self, obj):
        if self.objects_AVLTreeinside.search(obj.object_id):
            self.objects_AVLTreeinside.delete(obj.object_id)
            self.capacity += obj.size
            return
        return None
