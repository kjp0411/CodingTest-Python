# https://www.acmicpc.net/problem/2252
from collections import deque
N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)    # 진입 차수 리스트

for i in range(M):
    S, E = map(int, input().split())
    A[S].append(E)
    indegree[E] += 1    # 진입 차수 데이터 저장

queue = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:    # 위상 정렬 수행
    now = queue.popleft()
    print(now, end=' ')
    for next in A[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)