class BSTree:
    class Node:
        def __init__(self, key, val, left=None, right=None):
            self.key = key
            self.val = val
            self.left = left
            self.right = right
            
    def __init__(self):
        self.size = 0
        self.root = None
        
    def __getitem__(self, key):
        def getItem_rec(t):
            if t is None:
                raise KeyError
            elif t.key == key:
                return t.val
            elif t.key < key:
                return getItem_rec(t.right)
            else:
                return getItem_rec(t.left)
        return getItem_rec(self.root)
    
    def __setitem__(self, key, val):
        assert(key not in self)
        def setItem_rec(t):
            if t is None:
                return BSTree.Node(key=key, val=val)
            elif t.key > key:
                t.left = setItem_rec(t.left)
            else:
                t.right= setItem_rec(t.right)
            return t
        self.root = setItem_rec(self.root)
        self.size +=1
        
    def __delitem__(self, key):
        assert(key in self)
        # deal with relatively simple cases first!
        def delitem_rec(t):
            if key < t.key:
                t.left = delitem_rec(t.left)
            elif key > t.key:
                t.right = delitem_rec(t.right)
            else: #node containing the value we want to remove 
                if not t.left and not t.right: #most trivial cases, no right and left  
                    return None # return to the appropriate recursive call, which will set appropraitely right or left
                elif t.left and not t.right:
                    return t.left
                elif t.right and not t.left:
                    return t.right
                else:
                    to_del = t.left
                    if not to_del.right:
                        t.left = to_del.left
                    else:
                        p = to_del
                        to_del = to_del.right
                        while to_del.right:
                            p = to_del
                            to_del = to_del.right
                        p.right = to_del.left                     
                    t.val = to_del.val
            return t
        self.root = delitem_rec(self.root)
        self.size -=1
        
    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        def iter__rec_(t):
            if t is None:
                return 
            else:
                yield from iter__rec_(t.left) #Means the same as above
                yield t.key
                yield from iter__rec_(t.right) #Means the same as above
            
        return iter__rec_(self.root);
        
    def keys(self):
        return iter(self)

    def values(self):
        def iter__rec_(t):
            if t is None:
                return 
            else:
                yield from iter__rec_(t.left) #Means the same as above
                yield t.val
                yield from iter__rec_(t.right) #Means the same as above
            
        return iter__rec_(self.root);

    def items(self):
        def iter__rec_(t):
            if t is None:
                return 
            else:
                yield from iter__rec_(t.left) #Means the same as above
                yield (t.key, t.val)
                yield from iter__rec_(t.right) #Means the same as above
            
        return iter__rec_(self.root);
        
    def pprint(self, width=64):
        """Attempts to pretty-print this tree's contents."""
        height = self.height()
        nodes  = [(self.root, 0)]
        prev_level = 0
        repr_str = ''
        while nodes:
            n,level = nodes.pop(0)
            if prev_level != level:
                prev_level = level
                repr_str += '\n'
            if not n:
                if level < height-1:
                    nodes.extend([(None, level+1), (None, level+1)])
                repr_str += '{val:^{width}}'.format(val='-', width=width//2**level)
            elif n:
                if n.left or level < height-1:
                    nodes.append((n.left, level+1))
                if n.right or level < height-1:
                    nodes.append((n.right, level+1))
                repr_str += '{val:^{width}}'.format(val=n.key, width=width//2**level)
        print(repr_str)
    
    def height(self):
        """Returns the height of the longest branch of the tree."""
        def height_rec(t):
            if not t:
                return 0
            else:
                return max(1+height_rec(t.left), 1+height_rec(t.right))
        return height_rec(self.root)