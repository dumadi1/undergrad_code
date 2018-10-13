class Heap:
    def __init__(self, key=lambda x:x):
        self.data = []
        self.key  = key

    @staticmethod
    def _parent(idx):
        return (idx-1)//2
        
    @staticmethod
    def _left(idx):
        return idx*2+1

    @staticmethod
    def _right(idx):
        return idx*2+2
    
    def heapify(self, idx=0):
        l_idx = Heap._left(idx) #left idx
        r_idx = Heap._right(idx) #right idx
        while True:
            max_idx = idx
            if l_idx < len(self.data) and self.key(self.data[max_idx]) < self.key(self.data[l_idx]):
                max_idx = l_idx
            
            if  r_idx < len(self.data) and self.key(self.data[max_idx]) < self.key(self.data[r_idx]):
                max_idx = r_idx
            
            if max_idx != idx:
                self.data[max_idx], self.data[idx] = self.data[idx], self.data[max_idx]
                idx = max_idx
                l_idx = Heap._left(max_idx)
                r_idx = Heap._right(max_idx)
            
            else:
                break
            
    def add(self, x):
        self.data.append(x)
        idx = len(self.data) -1
        par = Heap._parent(idx)
        while idx > 0 and self.key(self.data[par]) < self.key(self.data[idx]): 
            self.data[par], self.data[idx] = self.data[idx], self.data[par]
            idx = par
            par = Heap._parent(par)
        
    def peek(self):
        assert(self)
        return self.data[0]

    def pop(self):
        ret = self.data[0]
        self.data[0] = self.data[len(self.data)-1]
        del self.data[len(self.data)-1]
        self.heapify()
        return ret
    
    def __bool__(self):
        return len(self.data) > 0

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)