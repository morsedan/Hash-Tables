# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # make a LinkedPair
        # hash the key.
        # get current
        hashed_key = self._hash_mod(key)
        linked_pair = LinkedPair(key, value)
        current = self.storage[hashed_key]
        # if the storage[hashed_key] isn't already None:
        if current is not None:
            if current.key == key:
                current.value = value # should be LinkedPair
                return
            #   while storage[hashed_key].next is not None:
            while current.next is not None:
                current = current.next
                if current.key == key:
                    current.value = value
                    return
            #       get next pair


        #   next pair.next = line 57
            current.next = linked_pair
        # else:
        else:
        #   storage[hashed_key] = LinkedPair
            self.storage[hashed_key] = linked_pair


# while current:
#     if current.key == key:
#         self.storage[hashed_key] = value
#         return
#     else:
#         current = current.next
#
# current = self.storage[hashed_key]
#
# if current:
#     while current.next:
#         current = current.next
#     current.next = linked_pair
# else:
#     self.storage[hashed_key] = linked_pair


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash_mod(key)
        # if self.storage[hashed_key] is None:
        #     print("Key not found")
        self.storage[hashed_key] = None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash_mod(key)
        linked_pair = self.storage[hashed_key]

        while linked_pair:
        # print("retrieve", key, linked_pair.key)
            if linked_pair.key == key:
                # print(linked_pair.value)
                return linked_pair.value
            else:
                linked_pair = linked_pair.next
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        old_storage = self.storage
        self.storage = new_storage
        for node in old_storage:
            while node:
                self.insert(node.key, node.value)
                node = node.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print("*** Before Overwrite ***")
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    ht.insert("line_1", "Bigger now?")
    ht.insert("line_2", "Overwritten?")
    ht.insert("line_3", "new value?")
    print("*** After ***")
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print("")
ht = HashTable(2)
ht.insert("Key", "aValue")
ht.insert("other key", "other value")
print(ht.retrieve("Key"))
print(ht.retrieve("other key"))
"""
1  2  3  4  5  6  7  8  9
2  4  6  8  10 12 14 16 18
3 6 9 12 15 18 21 24 27 30
4
5
6
7
8
9

1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
"""