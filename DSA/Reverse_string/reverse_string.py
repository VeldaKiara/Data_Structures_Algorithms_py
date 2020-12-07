class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items
    
def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
        rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
        return rev_str
      
    
    return rev_str
input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str))

#output should be welcome to educative

'''
 for loop on line 22 iterates over
 input_str and pushes each character on to stack.
 
 we initialize rev_str as an empty string. We pop off 
 all the elements from the stack and append 
 them to rev_str one by one on line 24
 until the stack becomes empty and terminates the while loop on line 23.
 We return the rev_str on line 27.
 
'''