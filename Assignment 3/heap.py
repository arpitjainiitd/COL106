#CLASS HEAP
'''
Python Code to implement a heap with general comparison function
'''

class Heap:
    '''
    Class to implement a heap with a general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Initializes a heap with a comparison function.
        '''
        self.comparison_function = comparison_function
        self.myheap_array = init_array.copy()
        self.myheap_size = len(init_array)

        # Build the heap using heapify
        for i in range(self.myheap_size//2 - 1, -1, -1):
            self.Heapify(i)
    
    def Heapify(self, i):
        '''
        Maintains the heap property starting from index i downwards.
        '''
        left = self.Left(i)
        right = self.Right(i)
        smallest = i
        
        if left < self.myheap_size and self.comparison_function(self.myheap_array[left], self.myheap_array[smallest]):
            smallest = left
        if right < self.myheap_size and self.comparison_function(self.myheap_array[right], self.myheap_array[smallest]):
            smallest = right
            
        if smallest != i:
            # Swap and heapify the affected subtree
            self.myheap_array[i], self.myheap_array[smallest] = self.myheap_array[smallest], self.myheap_array[i]
            self.Heapify(smallest)

    def Parent(self, i):
        return (i - 1) // 2
        
    def Left(self, i):
        return 2 * i + 1
        
    def Right(self, i):
        return 2 * i + 2

    def insert(self, value):
        '''
        Inserts a value into the heap.
        '''
        self.myheap_array.append(value)
        self.myheap_size += 1
        i = self.myheap_size - 1
        
        # Restore the heap property by moving up
        while i > 0 and self.comparison_function(self.myheap_array[i], self.myheap_array[self.Parent(i)]):
            self.myheap_array[i], self.myheap_array[self.Parent(i)] = self.myheap_array[self.Parent(i)], self.myheap_array[i]
            i = self.Parent(i)
    
    def extract(self):
        '''
        Extracts and returns the top value of the heap.
        '''
        if self.myheap_size <= 0:
            return None
        if self.myheap_size == 1:
            self.myheap_size -= 1
            return self.myheap_array.pop(0)
        
        root = self.myheap_array[0]
        # Move the last element to the root and heapify
        self.myheap_array[0] = self.myheap_array.pop()
        self.myheap_size -= 1
        self.Heapify(0)
        return root

    def top(self):
        '''
        Returns the top value of the heap without removing it.
        '''
        if self.myheap_size > 0:
            return self.myheap_array[0]
        return None
