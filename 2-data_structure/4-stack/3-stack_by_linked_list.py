class Node:
    
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next= next
        self.prev = None
    
    def __str__(self) -> str:
        return str(self.value)
    

class Stack:

    def __init__(self) -> None:
        self.head : Node  = None 
        self.size = 0 
    
    # O(1)
    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node 
        self.size += 1
    # O(1)  
    def pop(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
            return value 
        else:
            raise IndexError('pop from empty stack') 
    # O(1)
    def peek(self):
        if self.head:
            return self.head.value 
    # O(1)
    def is_empty(self):
        return self.size == 0 
    # O(1)
    def __len__(self):
        return self.size 
    
    # O(n)
    def __str__(self) -> str:
        l = [None] * self.size
        current = self.head
        index = self.size - 1
        while current:
            l[index] = current.value
            current = current.next 
            index -= 1
        return str(l)
    

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.push(3)
print(stack)
print(len(stack))