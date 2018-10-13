# <GRADED>
class OrderedHashtable:
    class Node:
        """This class is used to create nodes in the singly linked "chains" in
        each hashtable bucket."""

        def __init__(self, index, next=None):
            # don't rename the following attributes!
            self.index = index
            self.next = next

    def __init__(self, n_buckets=1000):
        # the following two variables should be used to implement the "two-tiered"
        # ordered hashtable described in class -- don't rename them!
        self.indices = [None] * n_buckets
        self.entries = []
        self.count = 0

    def __getitem__(self, key):
        hidx = self.index = hash(key) % len(self.indices)
        curr = self.indices[hidx]
        while curr:
            if self.entries[curr.index][0] == key:
                return self.entries[curr.index][1]
            else:
                curr = curr.next
        else:
            raise KeyError

    def __setitem__(self, key, val):
        hidx = hash(key) % len(self.indices)
        self.entries.append([key, val])
        self.indices[hidx] = OrderedHashtable.Node(
            self.count, next=self.indices[hidx])
        self.count += 1

    def __delitem__(self, key):
        hidx = hash(key) % len(self.indices)
        hidx = self.indices[hidx]
        while hidx:
            if self.entries[hidx.index][0] == key:
                self.entries[hidx.index][0] = None
            hidx = hidx.next

    def __contains__(self, key):
        try:
            _ = self[key]
            return True
        except:
            return False

    def __len__(self):
        return self.count

    def __iter__(self):
        for kv in self.indices:
            while kv is not None:
                yield kv.key
                kv = kv.next

    def keys(self):
        return iter(self)

    def values(self):
        for kv in self.indices:
            while kv is not None:
                yield kv.val
                kv = kv.next

    def items(self):
        for kv in self.indices:
            while kv is not None:
                yield (kv.key, kv.val)
                kv = kv.next

    def __str__(self):
        return '{ ' + ', '.join(str(k) + ': ' + str(v) for k, v in self.items()) + ' }'

    def __repr__(self):
        return str(self)
# </GRADED>
