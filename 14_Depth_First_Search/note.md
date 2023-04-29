### Topological Sort

위상 정렬(Topological Sort)은 방향 그래프의 모든 노드를 방향성에 따라 정렬하는 알고리즘이다. 위상 정렬은 그래프의 순환(cycle)이 없는 유향 그래프(directed acyclic graph)에서만 가능하다.

위상 정렬의 작동 원리는 각 노드들의 선행 조건(predecessor)을 파악하여, 그래프에 있는 모든 노드들을 선행 조건을 만족하는 순서대로 정렬하는 것이다. 만약 그래프에 순환(cycle)이 존재한다면, 선행 조건을 만족시킬 수 없어 위상 정렬이 불가능하다.

위상 정렬의 구현 방법은 일반적으로 DFS(Depth-First Search)나 BFS(Breadth-First Search)를 이용한다. DFS를 이용할 경우, 그래프의 모든 노드를 한번씩 방문하면서 각 노드의 선행 조건을 만족하는 순서대로 스택에 삽입하면 된다. BFS를 이용할 경우, 그래프의 노드들을 위상 순서에 맞게 큐에 삽입하여 구현할 수 있다.

위상 정렬은 작업 스케줄링, 의존 관계 파악, 컴파일러 설계 등 다양한 분야에서 사용되며, 그래프 이론에서 중요한 알고리즘 중 하나이다.

### Reference:

- https://seanprashad.com/leetcode-patterns/
- https://www.youtube.com/watch?v=_hxFgg7TLZQ
- 프로그래머가 알아야 할 알고리즘 40
- https://youtu.be/GC-nBgi9r0U
- Data Structure Algorithms Python (Book)
- O'Reilly Learning Algorithms (Book)
- 40 Algorithms Every Programmer Should Know (Book)
