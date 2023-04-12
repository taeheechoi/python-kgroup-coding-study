### Table Doubling
```python
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
```
해시 테이블은 __setitem__ 메서드를 사용하여 구현되며, 키를 해싱하여 인덱스를 가져옵니다. 만약 해당 인덱스가 이미 사용 중이라면, 알고리즘은 선형 방식으로 다음 빈 슬롯을 탐색합니다. 만약 해시 테이블의 로드 팩터(해시 테이블의 용량 대비 아이템 수의 비율)가 0.7을 초과한다면, 해시 테이블의 용량을 두 배로 늘립니다.

__getitem__ 메서드를 사용하여 해시 테이블에서 아이템을 검색할 때는, 키를 해싱하여 인덱스를 가져옵니다. 해당 인덱스의 슬롯이 비어 있거나 다른 키를 가지고 있다면, 알고리즘은 선형 방식으로 다음 슬롯을 탐색합니다. 모든 슬롯을 탐색한 후에도 슬롯이 여전히 비어 있거나 다른 키를 가지고 있다면, KeyError를 발생시킵니다.

__delitem__ 메서드를 사용하여 해시 테이블에서 아이템을 삭제할 때는, 키를 해싱하여 인덱스를 가져옵니다. 해당 인덱스의 슬롯이 비어 있거나 다른 키를 가지고 있다면, 알고리즘은 선형 방식으로 다음 슬롯을 탐색합니다. 모든 슬롯을 탐색한 후에도 슬롯이 여전히 비어 있거나 다른 키를 가지고 있다면, KeyError를 발생시킵니다. 그렇지 않다면, 아이템은 해당 슬롯에서 삭제되고, 로드 팩터가 0.2 미만이라면 해시 테이블의 용량이 축소됩니다.

전반적으로 이 구현은 선형 탐색을 사용하는 오픈 어드레싱 방식으로 충돌을 해결합니다. 그러나 이 방식은 클러스터링이 발생할 수 있는데, 이는 긴 슬롯 체인이 형성되어 해시 테이블의 성능을 저하시킬 수 있습니다. 이 문제를 해결하기 위해 다른 방식, 예를 들어 separate chaining이나 double hashing을 사용할 수 있습니다.