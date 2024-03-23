class Node:
    
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next= next
        self.prev = None
    
    def __str__(self) -> str:
        return str(self.value)
    


class Queue:
    
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = Node
        self.size = 0  
    
    # O(1)
    def enqueue(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node 
            self.tail = self.head
        else:
            self.tail.next = new_node 
            self.tail = new_node 
        self.size += 1
    
    # O(1)
    def dequeue(self):
        if self.head:
            value = self.head.value 
            self.head = self.head.next 
            self.size -= 1
            return value 
        else:
            raise IndexError("dequeue from empty queue") 
    
    # O(1)
    def peek(self):
        if self.head:
            return self.head.value
     
    # O(1)
    def __len__(self):
        return self.size 
    
    # O(1)
    def is_empty(self):
        return self.size == 0  
    
    # O(n)
    def __str__(self) -> str:
        l = []
        current = self.head
        while current:
            l.append(current.value)
            current = current.next
        return str(l)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()