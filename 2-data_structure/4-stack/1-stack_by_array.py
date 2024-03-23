
class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.head = 0
    
    # O(1)
    def push(self, value):
        self.stack.append(value)
        self.head += 1
    # O(1)
    def pop(self):
        value = self.stack.pop()
        self.head -= 1 
        return value 
    # O(1)
    def peek(self): 
        if self.stack:
            return self.stack(self.head -1)
    # O(1)
    def is_empty(self):
        return self.head == 0
    
    # O(1)
    def __len__(self):
        return self.head
    
    # O(n)   
    def __str__(self) -> str:
        return str(self.stack) 
    

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack)
print(len(stack))