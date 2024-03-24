
class Queue:
    
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = [] 
        
    
    def enqueue(self, value):
        for _ in range(len(self.s1)):
            self.s2.append(self.s1.pop())
        
        self.s1.append(value) 
        
        for _ in range(len(self.s2)):
            self.s1.append(self.s2.pop())
    
    def dequeue(self):
        if self.s1:
            return self.s1.pop() 
        else:
            raise IndexError('pop from empty queue')
    
    def __len__(self):
        return len(self.s1)
    
    def is_empty(self):
        return len(self.s1) == 0   
    
    def __str__(self) -> str:
        return str(self.s1)         
    

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