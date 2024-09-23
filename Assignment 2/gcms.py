from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException
from node import Node

class GCMS:
    def __init__(self):
        self.capacity_AVLTree = AVLTree()  # AVL Tree to manage bins by capacity
        self.ID_AVLTree = AVLTree() #AVL Tree to manage bins by ID
        self.objects_AVLTree = AVLTree()  # AVL Tree to manage objects by object_id

    def add_bin(self, bin_id, capacity):
        # Create a new bin and insert it into the AVL Tree
        new_bin = Bin(bin_id, capacity)
        if (self.capacity_AVLTree.search(capacity) == None):
            temptree = AVLTree()
            temptree.insert(bin_id, new_bin)
            self.capacity_AVLTree.insert(capacity, temptree)  

        else:
            node_with_same_capacity_in_capacityAVL = self.capacity_AVLTree.search(capacity)
            node_with_same_capacity_in_capacityAVL.value.insert(bin_id, new_bin)

        self.ID_AVLTree.insert(bin_id, new_bin)  # Insert based on ID_AVLTree


    def remove_entire_bin(self, capacity):
        tempbin = self.capacity_AVLTree.search(capacity)
        if tempbin is None or tempbin.value.root is not None:
            return
        else:
            self.capacity_AVLTree.delete(capacity)

    def add_object(self, object_id, size, color):
        curr = self.capacity_AVLTree.root
        reqd_node = None
        reqd_bin = None

        if curr is None:
            raise NoBinFoundException

        # BLUE
        if color == Color.BLUE:
            curr = self.capacity_AVLTree.find_successor_in_absence(curr, size)
        
        #YELLOW
        elif color == Color.YELLOW:
             curr = self.capacity_AVLTree.find_successor_in_absence(curr, size)

        # GREEN
        elif color == Color.GREEN:
            curr = self.capacity_AVLTree.maximum_in_subtree(curr)
        
        #RED
        elif color == Color.RED:
            curr = self.capacity_AVLTree.maximum_in_subtree(curr)

        # curr yahape desired capacity dhoondh chuka hai using compact/largest algo
        if ( color == Color.BLUE):
            if(curr is not None):
                reqd_node = curr.value.minimum_in_subtree(curr.value.root)

        elif ( color == Color.RED):
            if(curr is not None):
                reqd_node = curr.value.minimum_in_subtree(curr.value.root)

        elif (color == Color.GREEN):
            if(curr is not None):
                reqd_node = curr.value.maximum_in_subtree(curr.value.root)

        elif (color == Color.YELLOW):
            if(curr is not None):
                reqd_node = curr.value.maximum_in_subtree(curr.value.root)


        if reqd_node is None:
            raise NoBinFoundException

        reqd_bin = reqd_node.value

        new_object = Object(object_id, size, color)

        if reqd_bin.capacity < new_object.size:
            raise NoBinFoundException

        #delete the previous node and insert a new one with updated values for every AVLTree
        curr.value.delete(reqd_bin.bin_id)
        self.ID_AVLTree.delete(reqd_bin.bin_id)
        self.remove_entire_bin(reqd_bin.capacity)
        reqd_bin.add_object_for_bin(new_object)


        if (self.capacity_AVLTree.search(reqd_bin.capacity) == None):
            tree = AVLTree()
            tree.insert(reqd_bin.bin_id, reqd_bin)
            self.capacity_AVLTree.insert(reqd_bin.capacity, tree)  # Insert based on bin_id

        else:

            curr_found_node = self.capacity_AVLTree.search(reqd_bin.capacity)
            curr_found_node.value.insert(reqd_bin.bin_id, reqd_bin)

        self.ID_AVLTree.insert(reqd_bin.bin_id, reqd_bin)
        self.objects_AVLTree.insert(object_id, (new_object, reqd_bin))

        # print(f"Added Object:{object_id}, Size:{size}, Color: {color.name} in the bin {reqd_bin.bin_id}")

    def delete_object(self, object_id):
        node = self.objects_AVLTree.search(object_id)
        if node is None:
            return None

        reqd_obj= node.value[0]
        tempbin = node.value[1]
        now = self.capacity_AVLTree.search(tempbin.capacity)
        now.value.delete(tempbin.bin_id)
        self.remove_entire_bin(tempbin.capacity)
        self.ID_AVLTree.delete(tempbin.bin_id)
        tempbin.remove_object_from_bin(reqd_obj)


        if (self.capacity_AVLTree.search(tempbin.capacity) == None):
            tree = AVLTree()
            tree.insert(tempbin.bin_id, tempbin)
            self.capacity_AVLTree.insert(tempbin.capacity, tree)  # Insert based on bin_id

        else:

            curr_found_node = self.capacity_AVLTree.search(tempbin.capacity)
            curr_found_node.value.insert(tempbin.bin_id, tempbin)

        self.ID_AVLTree.insert(tempbin.bin_id, tempbin)

        self.objects_AVLTree.delete(object_id)
        # print(f"Object {object_id} removed from Bin {tempbin.bin_id}")

    def bin_info(self, bin_id):
        bin_node = self.ID_AVLTree.search(bin_id)
        if bin_node is not None:
            tempbin = bin_node.value
            return ((tempbin.capacity, tempbin.objects_AVLTreeinside.print_as_tuples()))
        else:
            # print(f"Bin {bin_id} not found")
            return None

    def object_info(self, object_id):
        node = self.objects_AVLTree.search(object_id)
        if node is not None:
            reqd_obj, tempbin = node.value
            return tempbin.bin_id
        else:
            # print(f"Object {object_id} not found")
            return None

    
    