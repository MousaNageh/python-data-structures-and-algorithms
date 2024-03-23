class Queue:
    
    def __init__(self) -> None:
        self.queue = {}
        self.size = 0 
    
    # O(1)
    def enqueue(self, value):
        self.queue[self.size] = value 
        self.size += 1
    
    # O(n)
    def dequeue(self):
        if self.queue:
            value = self.queue[self.size - 1]
            # will shift to the left 
            for i in range(self.size - 1):
                self.queue[i] = self.queue[i + 1]
            del self.queue[self.size - 1]
            self.size -= 1
            return value 
        else:
            raise IndexError("dequeue from empty queue") 
    
    # O(1)
    def peek(self):
        if self.queue:
            return self.queue[0]
     
    # O(1)
    def __len__(self):
        return self.size 
    
    # O(1)
    def is_empty(self):
        return self.size == 0  
    
    # O(n)
    def __str__(self) -> str:
        return str(list(self.queue.values()))


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