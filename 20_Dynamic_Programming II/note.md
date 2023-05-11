### 다이나믹 프로그래밍 단계

1. 하위 문제를 정의한다 - 하위 문제의 개수를 센다

- 주어진 문제를 부분 문제로 분할합니다.
- 부분 문제는 원래 문제보다 작고 해결하기 쉬운 문제여야 합니다.

2. 해의 일부를 추측한다 - 선택지의 개수를 센다

- 부분 문제를 해결하는 방법을 찾습니다.
- 이때, 부분 문제의 해결 방법이 부분 문제의 최적 해결 방법이어야 합니다.

3. 하위 문제의 해를 연관짓는다 - 하위 문제당 시간을 계산한다 (선택?)

4. 재귀 + 메모이제이션 - 시간 = 하위 문제당 시간 \* 하위 문제의 개수
   또는 DP 테이블을 상향식으로 만든다 - 하위 문제가 비순환이고 위상 순서 확인 필요하다

- 부분 문제를 해결하고 그 결과를 저장합니다.
- 이때, 중복 계산을 피하기 위해 결과를 저장해 둡니다.

5. 기존 문제를 푼다 - 하위 문제와 같거나 하위 문제의 해를 합쳐서 푼다.

- 저장된 결과를 이용하여 전체 문제를 해결합니다.
- 이때, 이전에 저장한 결과를 활용하여 중복 계산을 피합니다.

### Text Justification

```
words = ['Hello', 'world,', 'how', 'are', 'you', 'doing', 'today?']
L = 15

좋은 정렬
Hello world,
how are you
doing today?

나쁜 정렬
Hello
World,
How are
you
doing
today?
```

1. 하위 문제를 정의한다 - 하위 문제의 개수를 센다

- 접미사 단어[i:]의 나쁨을 최소화한다.
- 하위 문제 개수 = O(n:단어 개수)

2. 해의 일부를 추측한다 - 선택지의 개수를 센다

- 첫 줄을 어디서 끊을까 (i:j)

3. 하위 문제의 해를 연관짓는다 - 하위 문제당 시간을 계산한다 (선택?)

4. 재귀 + 메모이제이션 - 시간 = 하위 문제당 시간 \* 하위 문제의 개수
   또는 DP 테이블을 상향식으로 만든다 - 하위 문제가 비순환이고 위상 순서 확인 필요하다

- dp[i] = min(badness (i,j) + dp[j+1] for j in range (i, n))

5. 기존 문제를 푼다 - 하위 문제와 같거나 하위 문제의 해를 합쳐서 푼다.

- dp[0]

```python
assert word_wrap(['Hello', 'world,', 'how', 'are', 'you', 'doing', 'today?'], 15) == 25

# 123456789012345
# Hello world,___    ---> 3*3 (3 공백 수)
# how are you____    ---> 4*4 (4 공백 수)
# doing today?___    ---> 0 (마지막 줄)

```

```python
def compute_cost(words, i, j, L): # 함수는 i번째 단어부터 j번째 단어까지 한 줄에 나열했을 때, 해당 줄에 들어갈 문자열의 비용을 계산하는 함수

    length = sum([len(word) for word in words[i:j+1]]) + j - i # 줄의 길이를 계산하여 줄에있는 각 단어의 길이를 합하고 그 사이의 공백 수를 추가

    if j == len(words) - 1 and length <= L: # 줄이 단락의 마지막 줄이고 줄의 길이가 최대 너비보다 작거나 같으면 줄의 비용은 0
        return 0
    elif length > L:  # 줄의 길이가 최대 너비보다 크면 비용을 무한대로 설정하
        return float('inf')
    else:
        return (L - length) ** 2 # 줄의 길이가 최대 너비보다 작으면 최대 너비 L과 길이 length를 사용하여 비용. LaTex Rule, ^ 2 ^ 3 괜찮음

def word_wrap(words, L):
    n = len(words)

    dp = [0] * (n + 1)  # n+1 크기의 리스트 dp를 생성합니다. dp[i]는 i번째 단어부터 마지막 단어까지  한 줄로 출력할 때 필요한 최소 비용

    for i in range(n-1, -1, -1): # 마지막 단어 부터 시작
        cost = [compute_cost(words, i, j, L) + dp[j+1] for j in range(i, n)]

        dp[i] = min(cost)

    return dp[0] # dp[0]은 첫번째 단어부터 마지막 단어까지 한 줄로 출력할 때 필요한 최소 비용
```

이 구현의 시간 복잡도는 O (n ^ 2)입니다. 이는 각 단어가 다른 모든 단어와 비교되기 때문입니다.

### Perfect-Information Blackjack

- 블랙잭은 일반적으로 52장의 카드를 사용하는 카드 게임으로, 딜러와 하나 이상의 플레이어로 구성됩니다. 게임의 목표는 딜러의 점수를 능가하면서 21에 가까운 점수를 얻는 것입니다. 플레이어는 카드를 더 받을 수 있으며, 딜러는 일정한 규칙에 따라 카드를 받거나 받지 않습니다.
- 카드 값
  숫자 카드는 해당 카드의 숫자와 같은 점수를 가지며, K, Q, J는 각각 10점을, A는 1점 또는 11점 중 하나를 가집니다.
  무늬는 게임에서 중요하지 않습니다.
- 게임 진행
  딜러는 카드를 한 장씩 받고, 마지막 카드는 뒷면을 보이도록 받습니다.
  플레이어는 카드를 두 장 받고, 딜러의 한 장은 보이게 됩니다.
  플레이어는 카드를 더 받을지 결정할 수 있습니다. 이때, 카드의 합계가 21을 초과하면 바로 패배합니다.
  모든 플레이어가 카드를 받은 후, 딜러는 자신의 두 번째 카드를 보여줍니다.
  딜러는 자신의 카드 합계가 16 이하이면 카드를 더 받아야 하고, 17 이상이면 더 이상 카드를 받지 않습니다.
  딜러와 플레이어의 카드 합계를 비교하여, 21에 가까운 점수를 가진 쪽이 이기게 됩니다.
- 승패 결정
  플레이어가 21을 초과하면 바로 패배합니다.
  딜러가 21을 초과하면 플레이어가 이깁니다.
  플레이어와 딜러 모두 21점을 넘지 않으면, 카드 합계가 높은 쪽이 이깁니다.
  딜러와 플레이어의 카드 합계가 같으면 무승부가 됩니다.

1. 하위 문제를 정의한다 - 하위 문제의 개수를 센다

- i 는 이미 플레이한 카드 수, 남아 있는 카드 중(n)에 최고의 플레이를 선택한다.
- 하위 문제 개수 = O(n), 왜냐하면 i는 0 에서 n 까지

2. 해의 일부를 추측한다 - 선택지의 개수를 센다

- 참가자가 몇 장의 카드를 더 받는지, 선택 가능 수는 <= n, O(n) 추측할 수 있다.

3. 하위 문제의 해를 연관짓는다 - 하위 문제당 시간을 계산한다 (선택?)

4. 재귀 + 메모이제이션 - 시간 = 하위 문제당 시간 \* 하위 문제의 개수
   또는 DP 테이블을 상향식으로 만든다 - 하위 문제가 비순환이고 위상 순서 확인 필요하다

- BJ(i) = max(outcome ∈ {+1, 0, -1} + BJ(i + # cards used)) for # hits in 0,1 if valid play

5. 기존 문제를 푼다 - 하위 문제와 같거나 하위 문제의 해를 합쳐서 푼다.

- BJ(0)

```python
BJ(i):
    options = []
    if n-1 < 4: return 0, # since there are not enough cards
    for p in range(2, n-i-2): # number of cards taken
        # player’s cards by deal order (player, then dealer, then player)
        player = sum(c_i, c_{i+2}, c_{i+4:i+p+2})

        if player > 21: # bust
            options.append(-1 + BJ(i+p+2))
            break

        for d in range(2, n-i-p):
            dealer = sum(c_{i+1}, c_{i+3}, c_{i+p+2:i+p+d})
            if dealer >= 17: break
        if dealer > 21: dealer = 0 # bust
        options.append(cmp(player, dealer) + BJ(i+p+d))
    return max(options)

```

Finding the player and dealer sums each takes O(n). Looping over p takes O(n). Therefore, the whole thing takes O(n \*\* 2) time.

### Parent Pointers

다이나믹 프로그래밍을 사용할 때, 부분 문제의 해답을 기억하는 것만으로는 부분 문제의 해답을 재구성할 수 없는 경우가 있습니다. 이러한 경우, 부분 문제의 해답을 기억할 때 추가적인 정보를 저장하여 재구성이 가능하도록 만들어야 합니다.

이러한 추가 정보를 저장하는 방법은 여러 가지가 있습니다. 예를 들어, 부분 문제의 해답을 기억할 때, 그것의 부모를 포함한 2-튜플 형태로 기억할 수 있습니다. 이렇게 하면, 부분 문제의 해답을 기억할 때, 부모 포인터와 함께 기억할 수 있습니다. 이렇게 하면, 기억된 값이 사용될 때 항상 0번째 요소가 사용되어야 하므로, 부분 문제의 해답을 구할 때도 0번째 요소를 사용하면 됩니다. 이러한 방법을 사용하여 부분 문제의 해답을 기억하면, 원래 문제의 해답을 재구성하기 위해 부모 포인터를 사용하여 결과를 복원할 수 있습니다. 이를 위해서는, 방금 반환된 부모 포인터에서 시작하여, 이 부모 포인터를 따라 내려가면서 결과를 재구성하면 됩니다.

```python
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
    # 결과를 재구성
    fib_seq = [result]
    while parent is not None:
        fib_seq.append(parent)
        result, parent = memo[parent][0], memo[parent][1]
        fib_seq.append(result)
    # 재구성된 결과를 뒤집어서 반환
    return fib_seq[::-1]
```

위 코드에서는 memo 리스트를 사용하여 부분 문제의 해답과 부모 포인터를 기억합니다. 부분 문제 해답을 계산할 때는, 부모 포인터와 함께 이전 부분 문제의 해답을 사용하여 현재 부분 문제의 해답을 계산하고, 이를 memo 리스트에 저장합니다. 마지막으로, memo 리스트와 부모 포인터를 사용하여 결과를 재구성합니다.
