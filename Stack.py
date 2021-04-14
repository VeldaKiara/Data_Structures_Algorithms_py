#stack implementation
#create a stack
def create_stack():
    stack = []
    return stack
    
#create empty stack 
def check_empty(stack):
    return len(stack) == 0
    

#adding items to stack
def push(stack, item):
    stack.append(item)
    print("pushed item:" + item)
    

#removing items from a stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop()
    


stack = create_stack()
push(stack, "one")
push(stack, "Two")
push(stack, "Three")
push(stack, "Four")
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))


# output
# pushed item:one
# pushed item:Two
# pushed item:Three
# pushed item:Four
# popped item: Four
# stack after popping an element: ['one', 'Two', 'Three']

