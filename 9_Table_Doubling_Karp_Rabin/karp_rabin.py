def karp_rabin(text, pattern):
    n = len(text)  # 텍스트 문자열의 길이
    m = len(pattern)  # 패턴 문자열의 길이
    p = 31  # 해싱에 사용할 소수
    base = 256  # 입력 알파벳의 가능한 문자 수
    modulus = 10**9 + 9  # 해싱에 사용할 큰 소수
    
    # 패턴 문자열의 해시 값을 계산합니다.
    pattern_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % modulus
        print(pattern_hash)
    # 텍스트 문자열의 각 부분 문자열의 해시 값을 계산합니다.
    text_hash = [0] * (n - m + 1)
    print(text_hash)
    
    text_hash[0] = 0
    for i in range(m):
        text_hash[0] = (text_hash[0] * base + ord(text[i])) % modulus
        print('text_hash[0]', text_hash[0])
    
    for i in range(1, n - m + 1):
        text_hash[i] = ((text_hash[i-1] - ord(text[i-1]) * pow(base, m-1, modulus)) * base + ord(text[i+m-1])) % modulus
        print(f'text_hash[{i}]', text_hash[i])
    
    # 패턴 문자열과 각 부분 문자열의 해시 값을 비교합니다.
    for i in range(n - m + 1):
        print(i, pattern_hash,text_hash[i], pattern, text[i:i+m] )
        if pattern_hash == text_hash[i] and pattern == text[i:i+m]:
            return i
    
    # 일치하는 문자열이 없으면 -1을 반환합니다.
    return -1


print(karp_rabin('i love coding.', 'cod'))

# c: 99
# o: 25455
# d: 6516580
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# text_hash[0] 105
# text_hash[0] 26912
# text_hash[0] 6889580
# text_hash[1] 2124911
# text_hash[2] 7106422
# text_hash[3] 7304805
# text_hash[4] 7759136
# text_hash[5] 6627427
# text_hash[6] 2122607
# text_hash[7] 6516580
# text_hash[8] 7300201
# text_hash[9] 6580590
# text_hash[10] 6909543
# text_hash[11] 7235374
# 0 6516580 6889580 cod i l
# 1 6516580 2124911 cod  lo
# 2 6516580 7106422 cod lov
# 3 6516580 7304805 cod ove
# 4 6516580 7759136 cod ve
# 5 6516580 6627427 cod e c
# 6 6516580 2122607 cod  co
# 7 6516580 6516580 cod cod