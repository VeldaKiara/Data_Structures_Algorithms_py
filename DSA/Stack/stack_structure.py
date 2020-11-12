'''
stack structure
'''

class Stack ():
    #creating an empty stack
    def __init__ (self):
        self.items = [] 
    #push is definied as a function , to insert elements to the stack,
    #though we use append in py to add items 
    def push (self, item):
        self.items.append(item)
    #pop function to remove elements from a stack
    #pop is a py keyword
    def pop (self):
        return self.items.pop()
    #used to check if there elements in a stack
    def is_empty(self):
        return self.items == []
    # used to check if stack is not empty, prints last item
    def peek (self):
        if not self.is_empty():
            return self.items[-1]
    #prints the stack
    def get_stack (self):
        return self.items
    

myStack = Stack()
myStack.push("Velda")
myStack.push("Kiara")
myStack.push("Karimi")
myStack.pop()
print(myStack.peek())
    
            
    