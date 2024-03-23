

class Queue:
    
    def __init__(self) -> None:
        self.queue = []
        self.size = 0 
    
    # O(1)
    def enqueue(self, value):
        self.queue.append(value)
        self.size += 1
    
    # O(n)
    def dequeue(self):
        if self.queue:
            value = self.queue[0]
            # will shift the array O(n)
            del self.queue[0]
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
        return str(self.queue)