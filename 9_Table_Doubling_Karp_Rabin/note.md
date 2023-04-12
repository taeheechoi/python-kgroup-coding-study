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

### Θ?
컴퓨터 과학과 알고리즘 분석에서, 기호 "Θ" (theta로 발음)는 함수의 증가율의 점근적 상한과 하한을 나타내는 데 사용됩니다.

주어진 함수 f(n)에 대해, 어떤 최소값보다 큰 모든 n 값에 대해 c1g(n) <= f(n) <= c2g(n)인 두 개의 양의 상수 c1과 c2가 존재하면, f(n)은 Θ(g(n))의 순서를 갖는다고 말하고 f(n) = Θ(g(n))으로 쓴다.

더 간단하게 말하면, 이것은 f(n)의 증가율이 g(n)의 증가율과 일정한 상수 배수로 동일하다는 것을 의미합니다. 기호 Θ는 함수가 상수 배수 이상으로 빠르게 또는 느리게 성장하지 않는다는 의미로 타이트한 바운드를 나타내기 위해 사용됩니다.


### Θ(n + m) time = Θ(n) if m = Θ(n)
To prove that Θ(n + m) time = Θ(n) if m = Θ(n), we need to show that n + m and n are asymptotically equivalent when m is of the same order as n.

Assuming m = Θ(n), we can write m = cn for some positive constant c. Therefore, n + m = n + cn = (c+1)*n.

Now, we can see that n + m and n are asymptotically equivalent since they differ only by a constant factor (c+1). Thus, we can say that:

n + m = Θ(n) because n + m and n have the same growth rate (i.e., the same order of magnitude) when m = Θ(n).
Similarly, we can say that n = Θ(n + m) because n and n + m have the same growth rate when m = Θ(n).
Therefore, we have shown that Θ(n + m) time = Θ(n) if m = Θ(n).

###
1 + 2 + ··· + n = n(n+1)/2
1 + 2 + 4 + 8 + ··· + n =  2^0 + 2^1 + 2^2 + 2^3 + ··· + 2^k = 2^0(1 - 2^(k+1))/(1 - 2) = 2^0(1 - 2^(log₂n+1))/(1 - 2) = 2n - 1

y=2^(log₂n+1)
log₂y=log₂2^(log₂n+1)
log₂y=log₂n2log₂2
log₂y=log₂n
y=n

### Back to Hashing
만약 m = Θ(n)개의 버킷을 가지는 해시 테이블을 유지하고 간단한 균일 또는 유니버설 해싱을 사용한다면, 로드 팩터 α, 즉 각 버킷에 저장된 평균 항목 수는 Θ(1)입니다. 이것은 n개의 항목을 저장하기 위해 Θ(n)개의 버킷을 사용하기 때문입니다. 그러므로 버킷 당 평균 항목 수는 n/m = Θ(1)입니다.


### String Matching
grep -F 'word-to-search' file.txt

문자열 s가 문자열 t의 중요한 부분을 차지하는 상황에서는, O(|s|·(|t|−|s|))의 시간 복잡도가 제곱형태로 커질 가능성이 있으며, 최악의 경우 O(|s|·|t|)의 시간 복잡도를 가질 수 있습니다.

# Karp-Rabin Algorithm
해싱을 사용하여 패턴 문자열을 텍스트 문자열의 부분 문자열과 비교하는 문자열 매칭 알고리즘
```python
def karp_rabin(text, pattern):
    n = len(text)  # 텍스트 문자열의 길이, 검색 대상 문자열
    m = len(pattern)  # 패턴 문자열의 길이, 찾을 문자열
    p = 31  # 해싱에 사용할 소수
    base = 256  # 입력 알파벳의 가능한 문자 수
    modulus = 10**9 + 9  # 해싱에 사용할 큰 소수
    
    # 패턴 문자열의 해시 값을 계산합니다.
    pattern_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % modulus
    
    # 텍스트 문자열의 각 부분 문자열의 해시 값을 계산합니다.
    text_hash = [0] * (n - m + 1)
    text_hash[0] = 0
    for i in range(m):
        text_hash[0] = (text_hash[0] * base + ord(text[i])) % modulus
    for i in range(1, n - m + 1):
        text_hash[i] = ((text_hash[i-1] - ord(text[i-1]) * pow(base, m-1, modulus)) * base + ord(text[i+m-1])) % modulus
    
    # 패턴 문자열과 각 부분 문자열의 해시 값을 비교합니다.
    for i in range(n - m + 1):
        if pattern_hash == text_hash[i] and pattern == text[i:i+m]:
            return i
    
    # 일치하는 문자열이 없으면 -1을 반환합니다.
    return -1





```