# '''
# Linked List hash table key/value pair
# '''

"""
Notes:

# hash table has two parts:
#  {
#   array: [None, None, None],
#   hashFunction: ()
# }

Each position in the hash table data structure is often called
a slot or bucket and can store an element.

Each data item in the form of (key, value) pairs would be stored in the hash table
at a position that is decided by the hash value of the data.

A hash function is an index maker.
Make sure you can find the index again
but also make sure you're not accidentally double booking an index.

"""


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        """
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        """
        return hash(key)

    def _hash_djb2(self, key):
        """
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        """
        pass

    def _hash_mod(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        """

        # integer_index is the key that is hashed via _hash_mod method
        # (key used to find bucket items in hash table)
        integer_index = self._hash_mod(key)
        curr_key_value_pair = self.storage[integer_index]

        # print(integer_index)
        # print(curr_key_value_pair)

        while curr_key_value_pair is not None and curr_key_value_pair.key is not key:
            prev_pair = curr_key_value_pair
            curr_key_value_pair = prev_pair.next
        if curr_key_value_pair is not None:
            curr_key_value_pair.value = value
        else:
            new_node = LinkedPair(key, value)
            print(new_node.value)

            new_node.next = self.storage[integer_index]
            self.storage[integer_index] = new_node

    def remove(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        """
        integer_index = self._hash_mod(key)
        curr_key_value_pair = self.storage[integer_index]
        prev_pair = None
        while curr_key_value_pair is not None and curr_key_value_pair.key is not key:
            prev_pair = curr_key_value_pair
            curr_key_value_pair = prev_pair.next
        if curr_key_value_pair is None:
            print("Unable to remove item" + key)
        else:
            if prev_pair is None:
                self.storage[integer_index] = curr_key_value_pair.next
            else:
                prev_pair.next = curr_key_value_pair.next

    def retrieve(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        """
        integer_index = self._hash_mod(key)
        curr_key_value_pair = self.storage[integer_index]
        while curr_key_value_pair is not None:
            if curr_key_value_pair.key == key:
                return curr_key_value_pair.value
            curr_key_value_pair = curr_key_value_pair.next

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        """
        prev_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for slot_item in prev_storage:
            curr_key_value_pair = slot_item
            while curr_key_value_pair is not None:
                self.insert(curr_key_value_pair.key, curr_key_value_pair.value)
                curr_key_value_pair = curr_key_value_pair.next


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
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
