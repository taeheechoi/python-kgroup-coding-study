class HashTable:
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])

    def hash_function(self, key):
        return key % 8

    def insert(self, key, value):
        hash_value = self.hash_function(hash(key))
        self.hash_table[hash_value] = value

    def read(self, key):
        hash_value = self.hash_function(hash(key))
        return self.hash_table[hash_value]

    def print(self):
        print(self.hash_table)


ht = HashTable()
ht.insert(1, 'a')
ht.print()  # [0, 'a', 0, 0, 0, 0, 0, 0]
ht.insert('name', 'kang')
ht.print()  # [0, 'a', 'kang', 0, 0, 0, 0, 0]
ht.insert(2, 'b')  # 충돌 Collision
ht.print()  # [0, 'a', 'b', 0, 0, 0, 0, 0]
ht.insert(3, 'c')
ht.print()  # [0, 'a', 'b', 'c', 0, 0, 0, 0]
print(ht.read(2))  # b
ht.insert(4, 'd')
ht.print()  # [0, 'a', 'b', 'c', 'd', 0, 0, 0]

# 충돌 개선 법
# 1 Chaining (Open Hashing):
# 방법: 충돌 시, 링크드 리스트로 데이터를 추가로 연결, 기존 인덱스가 이미 사용중이면 해당 인덱스의 리스트에 추가하는 방법
# 단점: 공간 효율성이 떨어짐, 하나의 hash value index에 들어가면 불균형 구조 됨
class HashTableChaining:
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])

    def hash_function(self, key):
        return key % 8

    def insert(self, key, value):
      gen_key = hash(key)
      hash_value = self.hash_function(gen_key)

      if self.hash_table[hash_value] != 0:
          # 해당 hash value index를 이미 사용하고 있는 경우(충돌 시)
          for i in range(len(self.hash_table[hash_value])):
              # 이미 같은 키 값이 존재하는 경우 -> value 교체
              # 이때 0은 key, 1은 value값이 존재하는 인덱스
              if self.hash_table[hash_value][i][0] == gen_key:
                  self.hash_table[hash_value][i][1] = value
                  return
          # 같은 키 값이 존재하지 않는 경우에는 [key, value]를 해당 인덱스에 삽입
          self.hash_table[hash_value].append([gen_key, value])
      else:
          # 해당 hash_value를 사용하고 있지 않는 경우
          self.hash_table[hash_value] = [[gen_key, value]]

    def read(self, key):
      gen_key = hash(key)
      hash_value = self.hash_function(gen_key)

      if self.hash_table[hash_value] != 0:
          # 해당 해쉬 값 index에 데이터가 존재할 때,
          for i in range(len(self.hash_table[hash_value])):
              if self.hash_table[hash_value][i][0] == gen_key:
                  # 키와 동일할 경우 -> 해당 value return
                  return self.hash_table[hash_value][i][1]
          # 동일한 키가 존재하지 않으면 None return
          return None
      else:
          # 해당 해쉬 값 index에 데이터가 없을 때,
          return None
    
    def print(self):
        print(self.hash_table)

ht = HashTableChaining()
ht.insert(1, 'a')
ht.print()  # [0, [[1, 'a']], 0, 0, 0, 0, 0, 0]
ht.insert('name', 'kang')
ht.print()  # [0, [[1, 'a']], [[8053312755681375626, 'kang']], 0, 0, 0, 0, 0]
ht.insert(2, 'b')  # 충돌 Collision
ht.print()  # [0, [[1, 'a']], [[8053312755681375626, 'kang'], [2, 'b']], 0, 0, 0, 0, 0]
ht.insert(3, 'c')
ht.print()  # [0, [[1, 'a']], [[8053312755681375626, 'kang'], [2, 'b']], [[3, 'c']], 0, 0, 0, 0]
print(ht.read(2))  # b
ht.insert(4, 'd')
ht.print()  # [0, [[1, 'a']], [[8053312755681375626, 'kang'], [2, 'b']], [[3, 'c']], [[4, 'd']], 0, 0, 0]

# 2 Linear Probing (Closing Hashing)
# 방법: 충돌 시, has value를 다음 index부터 맨 처음 나오는 빈공간에 저장
# 단점: 미리 지정한 자릿 수 넘어가면 출동, 공간이 없음으로.
class HashTableCLinearProbing:
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])

    def hash_function(self, key):
        return key % 8

    def insert(self, key, value):
      gen_key = hash(key)
      hash_value = self.hash_function(gen_key)

      if self.hash_table[hash_value] != 0:
          # 해당 hash value index를 이미 사용하고 있는 경우(충돌 시)
          for i in range(hash_value, len(self.hash_table)):
              # 해당 hash value index부터 마지막 index까지
              # 돌면서 비어있거나 key가 같은 값을 찾는다.
              if self.hash_table[i] == 0:
                  # 해당 인덱스가 비어있을 때,
                  self.hash_table[i] = [gen_key, value]
                  return
              elif self.hash_table[i][0] == gen_key:
                  # 이미 같은 키 값이 존재하는 경우 덮어쓰기
                  self.hash_table[i][1] = value
                  return
      else:
          # 해당 hash_value를 사용하고 있지 않는 경우
          self.hash_table[hash_value] = [gen_key, value]

    def read(self, key):
      gen_key = hash(key)
      hash_value = self.hash_function(gen_key)

      if self.hash_table[hash_value] != 0:
          # 해당 해쉬 값 index에 데이터가 존재할 때,
          for i in range(hash_value, len(self.hash_table)):
              if self.hash_table[i] == 0:
                  # 비어있는 경우,
                  return None
              elif self.hash_table[i][0] == gen_key:
                  # 키와 동일할 경우 -> 해당 value return
                  return self.hash_table[i][1]
      else:
          # 해당 해쉬 값 index에 데이터가 없을 때,
          return None
    
    def print(self):
        print(self.hash_table)

ht = HashTableCLinearProbing()
ht.insert(1, 'a')
ht.print()  # [0, [1, 'a'], 0, 0, 0, 0, 0, 0]
ht.insert('name', 'kang')
ht.print()  # [0, [1, 'a'], [-5457085546329511295, 'kang'], 0, 0, 0, 0, 0]
ht.insert(2, 'b')  # 충돌 Collision
ht.print()  # [0, [1, 'a'], [-5457085546329511295, 'kang'], [2, 'b'], 0, 0, 0, 0]
ht.insert(3, 'c')
ht.print()  # [0, [1, 'a'], [-5457085546329511295, 'kang'], [2, 'b'], [3, 'c'], 0, 0, 0]
print(ht.read(2))  # b
ht.insert(4, 'd')
ht.print()  # [0, [1, 'a'], [-5457085546329511295, 'kang'], [2, 'b'], [3, 'c'], [4, 'd'], 0, 0]

# 3 공간 확장: Linear Probing + 공간 확장
# class HashTable:
#      def __init__(self, n):
#         self.n = n
#         self.hash_table = list([0 for i in range(n)])

#      def hash_function(self, key):
#          # Custom Hash Function
#          return key % self.n