class LinkedList:
    class Node:
        def __init__(self, val, prior=None, next=None):
            self.val = val
            self.prior = prior
            self.next  = next
    
    def __init__(self):
        self.head = LinkedList.Node(None) # sentinel node (never to be removed)
        self.head.prior = self.head.next = self.head # set up "circular" topology
        self.length = 0
        
        
    ### prepend and append, below, from class discussion
        
    def prepend(self, value):
        n = LinkedList.Node(value, prior=self.head, next=self.head.next)
        self.head.next.prior = self.head.next = n
        self.length += 1
        
    def append(self, value):
        n = LinkedList.Node(value, prior=self.head.prior, next=self.head)
        n.prior.next = n.next.prior = n
        self.length += 1
            
            
    ### subscript-based access ###
    
    def _normalize_idx(self, idx):
        nidx = idx
        if nidx < 0:
            nidx += len(self)
            if nidx < 0:
                nidx = 0
        return nidx
    
    def __getitem__(self, idx):
        """Implements `x = self[idx]`"""
        assert(isinstance(idx, int))
        n = self.get_node(idx)
        return n.val
    
    def get_node(self, idx):
        nidx = self._normalize_idx(idx)
        if(nidx >= self.length):
            raise IndexError()
        n = self.head.next
        for i in range(nidx):
            n = n.next
        return n

    def __setitem__(self, idx, value):
        """Implements `self[idx] = x`"""
        assert(isinstance(idx, int))
        n = self.get_node(idx) 
        newNode = LinkedList.Node(val = value, prior = n.prior, next = n.next)
        n.next.prior =  n.prior.next = newNode
        
    def __delitem__(self, idx):
        """Implements `del self[idx]`"""
        assert(isinstance(idx, int))
        n = self.get_node(idx) 
        n.next.prior = n.prior
        n.prior.next = n.next
        self.length -=1
        

    ### stringification ###
    
    def __str__(self):
        """Implements `str(self)`. Returns '[]' if the list is empty, else
        returns `str(x)` for all values `x` in this list, separated by commas
        and enclosed by square brackets. E.g., for a list containing values
        1, 2 and 3, returns '[1, 2, 3]'."""
        # YOUR CODE HERE
        return self.__repr__()
        
    def __repr__(self):
        """Supports REPL inspection. (Same behavior as `str`.)"""
        return '[' + ', '.join(str(x) for x in self) + ']'


    ### single-element manipulation ###
        
    def insert(self, idx, value):
        """Inserts value at position idx, shifting the original elements down the
        list, as needed. Note that inserting a value at len(self) --- equivalent
        to appending the value --- is permitted. Raises IndexError if idx is invalid."""
        assert(isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        
        if nidx == self.length:
            self.append(value)
        else:
            self.length +=1
            n = self.head.next
            for i in range(nidx):
                n = n.next
            newNode = LinkedList.Node(val = value, next = n, prior =n.prior)
            n.prior.next = n.prior = newNode
            
    def pop(self, idx=-1):
        """Deletes and returns the element at idx (which is the last element,
        by default)."""
        to_ret =  self.__getitem__(idx)
        self.__delitem__(idx)
        return to_ret
    
    def remove(self, value):
        """Removes the first (closest to the front) instance of value from the
        list. Raises a ValueError if value is not found in the list."""
        for i in range(self.length):
            if self[i] == value:
                self.__delitem__(i)
                return
        raise ValueError
    

    ### predicates (T/F queries) ###
    
    def __eq__(self, other):
        """Returns True if this LinkedList contains the same elements (in order) as
        other. If other is not an LinkedList, returns False."""
        if not isinstance(other, LinkedList):
            return False
        if len(other) != len(self):
            return False
        j =0
        for i in other:
            if i != self[j]:
                return False
            j +=1
        return True

    def __contains__(self, value):
        """Implements `val in self`. Returns true if value is found in this list."""
        for i in self:
            if value == i: 
                return True
        return False


    ### queries ###
    
    def __len__(self):
        """Implements `len(self)`"""
        return self.length
    
    def min(self):
        """Returns the minimum value in this list."""
        # YOUR CODE HERE
        min = self[0]
        for i in self:
            if i < min:
                min = i
        return min
            
    def max(self):
        """Returns the maximum value in this list."""
        max = self[0]
        for i in self:
            if i > max:
                max = i
        return max
    
    def index(self, value, i=0, j=None):
        """Returns the index of the first instance of value encountered in
        this list between index i (inclusive) and j (exclusive). If j is not
        specified, search through the end of the list for value. If value
        is not in the list, raise a ValueError."""
        if j is None:
            for i in range(i, len(self)):
                if self[i] == value:
                    return i
        else:
            i = self._normalize_idx(i)
            j = self._normalize_idx(j)
            for i in range(i, j):
                if self[i] == value:
                    return i
        raise ValueError
    
    def count(self, value):
        """Returns the number of times value appears in this list."""
        count = 0
        for i in self:
            if i == value:
                count +=1 
        return count

    
    ### bulk operations ###

    def __add__(self, other):
        """Implements `self + other_list`. Returns a new LinkedList
        instance that contains the values in this list followed by those 
        of other."""
        assert(isinstance(other, LinkedList))
        to_ret = LinkedList()
        for i in self:
            to_ret.append(i)
        for j in other:
            to_ret.append(j)
        return to_ret
    
    def clear(self):
        """Removes all elements from this list."""
        for _ in range(self.length):
            self.__delitem__(-1)
        
    def copy(self):
        """Returns a new LinkedList instance (with separate Nodes), that
        contains the same values as this list."""
        to_ret = LinkedList()
        return self.__add__(to_ret)

    def extend(self, other):
        """Adds all elements, in order, from other --- an Iterable --- to this list."""
        for i in other:
            self.append(i)

            
    ### iteration ###

    def __iter__(self):
        """Supports iteration (via `iter(self)`)"""
        n = self.head.next
        while n is not self.head:
            yield n.val 
            n = n.next