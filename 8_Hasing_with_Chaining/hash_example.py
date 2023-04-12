import hashlib

data = 'test'.encode()
print(data) # b'test'
hash_object = hashlib.sha1()
hash_object.update(data)
print(hash_object) # <sha1 HASH object @ 0x104498eb0>
hex_dig = hash_object.hexdigest()
print(hex_dig) # a94a8fe5ccb19ba61c4c0873d391e987982fbbd3

data = 'test'.encode()
print(data) # b'test'
hash_object = hashlib.sha256()
hash_object.update(data)
print(hash_object) # <sha1 HASH object @ 0x104498eb0>
hex_dig = hash_object.hexdigest()
print(hex_dig) # 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08

# 해쉬 함수
def hash_function(key):
    return key % 8

data = 'test'
print(hash(data)) # 3149808501497212018
print(hash_function(hash(data))) # 0

data = 111
print(hash(data)) # 1
print(hash_function(hash(data))) # 1

# 중복 주의
a = {1: 'a', 1: 'b'}
print(a) # {1: 'b'}

