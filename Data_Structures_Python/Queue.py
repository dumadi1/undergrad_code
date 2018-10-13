class Queue:
    def __init__(self, limit=10):
        self.data = [None] * limit
        self.head = -1
        self.tail = -1
        
    def enqueue(self, val):
        if self.tail == len(self.data)-1: #if at last position, wrap
            if self.data[0] == None: 
                self.tail = 0
                self.data[self.tail] = val
            else:
                raise RuntimeError
            
        elif self.data[self.tail + 1] == None: #if the one after the current one is None, you can append
            self.tail +=1
            self.data[self.tail] = val
        else:
            raise RuntimeError
        
    def dequeue(self):
        if self.head == -1:
            self.head=0
        if self.data[self.head] != None:
            if self.head == len(self.data)-1: #if at last position, wrap
                to_ret = self.data[self.head]
                self.data[self.head] = None
                self.head = 0
            else:    
                to_ret = self.data[self.head]
                self.data[self.head] = None
                self.head +=1
            if self.empty():
                self.head = -1
                self.tail = -1
            return to_ret
        else:
            raise RuntimeError
    
    def resize(self, newsize):
        new = []
        
        for i in self:
            if i != None:
                 new.append(i)
                    
        self.head = 0
        self.tail = len(new) -1
        
        while len(new) < newsize:
            new.append(None)
        self.data = new
                
    def empty(self):
        for i in self.data:
            if i == None:
                pass
            else:
                return False
        return True
    
    def __bool__(self):
        return not self.empty()
    
    def __str__(self):
        if not(self):
            return ''
        return ', '.join(str(x) for x in self)
    
    def __repr__(self):
        return str(self)
    
    def __iter__(self):
        start = self.head
        if self.head > self.tail:
            right = len(self.data) - (self.head + 1)
            left = len(self.data) - right
            num = left + right
        elif self.head < self.tail:
            num = self.head - self.tail
        else: 
            num =0
        for i in range(num):
            if start == len(self.data)-1:
                if self.data[start] != None:
                    yield self.data[start]
                start =0
            else:
                if self.data[start] != None:
                    yield self.data[start]
                start +=1