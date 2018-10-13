class ArrayList:
    def __init__(self):
        self.data = ConstrainedList() # don't change this line!

    
    ### subscript-based access ###
    
    def _normalize_idx(self, idx):
        nidx = idx
        if nidx < 0:
            nidx += len(self.data)
            if nidx < 0:
                ndix =0
        return nidx
    
    def __getitem__(self, idx):
        """Implements `x = self[idx]`"""
        assert(isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        if nidx >= len(self.data):
            raise IndexError
        return self.data[nidx]

    def __setitem__(self, idx, value):
        """Implements `self[idx] = x`"""
        assert(isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        if nidx >= len(self.data):
            raise IndexError
        self.data[nidx] = value

    def __delitem__(self, idx):
        """Implements `del self[idx]`"""
        assert(isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        if nidx >= len(self.data):
            raise IndexError
        for i in range(nidx+1, len(self.data)):
            self.data[i-1] = self.data[i]
        del self.data[len(self.data)-1]
    

    ### stringification ###
    
    def __str__(self):
        """Implements `str(self)`. Returns '[]' if the list is empty, else
        returns `str(x)` for all values `x` in this list, separated by commas
        and enclosed by square brackets. E.g., for a list containing values
        1, 2 and 3, returns '[1, 2, 3]'."""
        s =""
        if self.data is 0:
            return "[]"
        else:
            for i in range(len(self.data)):
                s += str(self.data[i])
                if i != len(self.data)-1:
                    s += ", "
        return "[" + s + "]"
    def __repr__(self):
        """Supports REPL inspection. (Same behavior as `str`.)"""
        return self.__str__()


    ### single-element manipulation ###
    
    def append(self, value):
        """Appends value to the end of this list."""
        self.data.append(None)
        self.data[len(self.data)-1] = value
    def insert(self, idx, value):
        """Inserts value at position idx, shifting the original elements down the
        list, as needed. Note that inserting a value at len(self) --- equivalent
        to appending the value --- is permitted. Raises IndexError if idx is invalid."""
        assert(isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        self.data.append(None)
        for i in range(len(self.data)-1,idx,-1):
            self.data[i] = self.data[i-1]
        self.data[idx] = value
        
    def pop(self, idx=-1):
        """Deletes and returns the element at idx (which is the last element,
        by default)."""
        to_ret =self. __getitem__(idx)
        self.__delitem__(idx)
        return to_ret
        
    def remove(self, value):
        """Removes the first (closest to the front) instance of value from the
        list. Raises a ValueError if value is not found in the list."""
        found = False
        for i in range(len(self.data)):
            if self.data[i] != value:
                pass
            else:
                found = True
                self.__delitem__(i)
                break
        if not found:
            raise ValueError

    ### predicates (T/F queries) ###
    
    def __eq__(self, other):
        """Returns True if this ArrayList contains the same elements (in order) as
        other. If other is not an ArrayList, returns False."""
        to_ret = False
        
        if (not isinstance(other, ArrayList)) or (len(other.data) != len(self.data)):
            return to_ret
        for i in range(len(self.data)):
            if self.data[i] != other.data[i]:
                return to_ret
            else:
                pass
        to_ret = True
        return to_ret
        

    def __contains__(self, value):
        """Implements `val in self`. Returns true if value is found in this list."""
        found = False
        for i in range(len(self.data)):
            if self.data[i] == value:
                return True
        return found


    ### queries ###
    
    def __len__(self):
        """Implements `len(self)`"""
        return len(self.data)
    
    def min(self):
        """Returns the minimum value in this list."""
        least = self.data[0]
        
        for i in range(len(self.data)):
            if self.data[i] < least:
                least = self.data[i]
        return least
    def max(self):
        """Returns the maximum value in this list."""
        most = self.data[0]
        
        for i in range(len(self.data)):
            if self.data[i] > least:
                most = self.data[i]
        return most
    def index(self, value, i=0, j=None):
        """Returns the index of the first instance of value encountered in
        this list between index i (inclusive) and j (exclusive). If j is not
        specified, search through the end of the list for value. If value
        is not in the list, raise a ValueError."""
        # YOUR CODE HERE
        raise NotImplementedError()
    
    def count(self, value):
        """Returns the number of times value appears in this list."""
        # YOUR CODE HERE
        raise NotImplementedError()

    
    ### bulk operations ###

    def __add__(self, other):
        """Implements `self + other_array_list`. Returns a new ArrayList
        instance that contains the values in this list followed by those 
        of other."""
        # YOUR CODE HERE
        raise NotImplementedError()
    
    def clear(self):
        self.data = ConstrainedList() # don't change this!
        
    def copy(self):
        """Returns a new ArrayList instance (with a separate data store), that
        contains the same values as this list."""
        # YOUR CODE HERE
        raise NotImplementedError()

    def extend(self, other):
        """Adds all elements, in order, from other --- an Iterable --- to this list."""
        # YOUR CODE HERE
        raise NotImplementedError()

            
    ### iteration ###
    
    def __iter__(self):
        """Supports iteration (via `iter(self)`)"""
        for i in range(len(self.data)):
            yield self.data[i]