def fib(n):
    memo = [None] * (n + 1)

    def fib_helper(n):
        if n <= 1:
            # 부모 포인터는 None으로 초기화
            return (n, None)
        if memo[n] is not None:
            # 기억된 값과 부모 포인터를 반환
            return memo[n]
        else:
            # 부분 문제 해답을 계산
            (a, a_parent) = fib_helper(n-1)
            (b, b_parent) = fib_helper(n-2)
            # 현재 부분 문제의 해답과 부모 포인터를 기억
            if a_parent is None:
                memo[n] = (a+b, n-1)
            else:
                memo[n] = (a+b, a_parent)
            # 부분 문제 해답과 부모 포인터를 반환
            return memo[n]

    result, parent = fib_helper(n)
    # print(result, parent, memo) # 8 1 [None, None, (1, 1), (2, 1), (3, 1), (5, 1), (8, 1)]
    #결과를 재구성
    fib_seq = [result]
    
    while parent is not None:
        fib_seq.append(parent)
        if memo[parent] is not None and memo[parent][1] is not None:
            result, parent = memo[parent][0], memo[parent][1]
        else:
            result, parent = 0, None
        fib_seq.append(result)
    # 재구성된 결과를 뒤집어서 반환
    return fib_seq[::-1]

print(fib(6))