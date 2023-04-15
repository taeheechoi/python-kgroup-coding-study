class HashTable:
    def __init__(self, initial_capacity=10):
        """
        Initialize the hash table with an initial capacity.
        """
        self.capacity = initial_capacity
        self.size = 0
        self.table = [None] * self.capacity

    def __setitem__(self, key, value):
        """
        Set an item in the hash table.
        """
        # Resize the hash table if it becomes too full.
        if (self.size / self.capacity) >= 0.7:
            self._resize(2 * self.capacity)

        # Hash the key to get an index.
        index = self._hash(key)

        # Probe for an empty slot or a slot with the same key.
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.capacity

        # If the slot is empty, increase the size of the hash table.
        if self.table[index] is None:
            self.size += 1

        # Set the item in the table.
        self.table[index] = (key, value)

    def __getitem__(self, key):
        """
        Get an item from the hash table.
        """
        # Hash the key to get an index.
        index = self._hash(key)

        # Probe for the slot with the given key.
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.capacity

        # If the slot is empty, the key is not in the table.
        if self.table[index] is None:
            raise KeyError(key)

        # Return the value associated with the key.
        return self.table[index][1]

    def __delitem__(self, key):
        """
        Delete an item from the hash table.
        """
        # Hash the key to get an index.
        index = self._hash(key)

        # Probe for the slot with the given key.
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.capacity

        # If the slot is empty, the key is not in the table.
        if self.table[index] is None:
            raise KeyError(key)

        # Delete the item from the table.
        self.table[index] = None
        self.size -= 1

        # Resize the hash table if it becomes too empty.
        if (self.size / self.capacity) <= 0.2:
            self._resize(self.capacity // 2)

    def _hash(self, key):
        """
        Hash a key to an index in the hash table.
        """
        return hash(key) % self.capacity

    def _resize(self, new_capacity):
        """
        Resize the hash table to a new capacity.
        """
        # Save the old table.
        old_table = self.table

        # Create a new table with the new capacity.
        self.capacity = new_capacity
        self.size = 0
        self.table = [None] * self.capacity

        # Insert the items from the old table into the new table.
        for item in old_table:
            if item is not None:
                self.__setitem__(item[0], item[1])