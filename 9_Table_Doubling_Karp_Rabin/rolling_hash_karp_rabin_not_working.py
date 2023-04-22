# Rolling Hash ADT
class RollingHash:
    def __init__(self, s, base=31, mod=10**9+9):
        self.s = s
        self.base = base
        self.mod = mod
        self.hash = self._hash(s)
        self.power = [1]
        for i in range(1, len(s)+1):
            self.power.append(self.power[-1]*base % mod)
    
    def _hash(self, s):
        h = 0
        for c in s:
            h = (h*self.base + ord(c)) % self.mod
        return h
    
    def append(self, c):
        self.s += c
        self.hash = (self.hash*self.base + ord(c)) % self.mod
    
    def skip(self):
        c = self.s[0]
        self.s = self.s[1:]
        self.hash = (self.hash - ord(c)*self.power[-1]) % self.mod
        self.power.pop()
    
    def get_hash(self):
        return self.hash


# Karp-Rabin 알고리즘
def karp_rabin(s, t):
    # 문자열 s와 t의 길이
    n, m = len(s), len(t)
    
    # s와 t의 해시값 계산
    hash_s = RollingHash(s).get_hash()
    rolling_hash_t = RollingHash(t[:n])
    hash_t = rolling_hash_t.get_hash()
    
    # s와 t의 해시값이 같은 위치를 찾음
    for i in range(m-n+1):
        if hash_s == hash_t:
            if s == t[i:i+n]:
                return i
        rolling_hash_t.skip()
        rolling_hash_t.append(t[i+n])
        hash_t = rolling_hash_t.get_hash()
    
    # s를 찾지 못한 경우
    return -1


# 테스트
def test():
    s = 'abc'
    t = 'abcdeabc'
    assert karp_rabin(s, t) == 0
    
    s = 'abc'
    t = 'bcdeabc'
    assert karp_rabin(s, t) == 4
    
    s = 'abc'
    t = 'ababcabc'
    assert karp_rabin(s, t) == 2
    
    s = 'abc'
    t = 'abab'
    assert karp_rabin(s, t) == -1
    
    s = 'abc'
    t = 'a' + 'b'*10**5 + 'c'
    assert karp_rabin(s, t) == 1
    
    print('테스트 통과!')


if __name__ == '__main__':
    test()
