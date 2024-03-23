class Stack:
    
    def __init__(self) -> None:
        self.stack = {}
        self.head = 0
    
    # O(1)
    def push(self, value):
        self.stack[self.head] = value
        self.head += 1
    
    def pop(self):
        if self.stack:
            value = self.stack[self.head - 1] 
            del self.stack[self.head - 1]
            self.head -= 1
            return value 
        else:
            raise IndexError('pop from empty stack')
     # O(1)
    def peek(self): 
        if self.stack:
            return self.stack[self.head -1]
     # O(1)
    def is_empty(self):
        return self.head == 0
    
     # O(1)
    def __len__(self):
        return self.head
    
    # O(n)  
    def __str__(self) -> str:
        return str(list(self.stack.values())) 
    

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.pop()
stack.pop()
print(stack.is_empty())