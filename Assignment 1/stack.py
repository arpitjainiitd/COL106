class Stack:
    # constructor function to initialise stack as a list
    def __init__(self) -> None: 
        self.stackarr = []          

    # adding an element into the stack 
    def push(self, data):
        self.stackarr.append(data)
    
    #removing the topmost element of stack
    def pop(self):
        if len(self.stackarr) != 0:
            self.stackarr.pop()
    
    #returning the current size of stacl
    def size(self):
        return len(self.stackarr)
    
    #returning the topmost element of stack
    def top(self):
        if len(self.stackarr) != 0:
            return self.stackarr[-1]

    #allowing the stack to be iterable
    def __iter__(self):
        return iter(self.stackarr)
