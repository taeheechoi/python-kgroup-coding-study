### Note
- 힙 property : A가 B의 부모노드이면 A의 키값과 B의 키값 사이에는 대소 관계가 성립한다

- 최소 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙

- 최대 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙

- 파이썬 heapq: 모든 부모 노드는 그의 자식 노드보다 값이 작거나 큰 이진트리(binary tree) 구조인데, 내부적으로는 인덱스 0에서 시작해 k번째 원소가 항상 자식 원소들(2k+1, 2k+2) 보다 작거나 같은 최소 힙의 형태로 정렬된다. 

- heapq.heappush(heap, item): item을 heap에 추가

- heapq.heappop(heap): heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 

- heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N))

### Reference
- https://littlefoxdiary.tistory.com/3
- https://www.toptal.com/developers/sorting-algorithms