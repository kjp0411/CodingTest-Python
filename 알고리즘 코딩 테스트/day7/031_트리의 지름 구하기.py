# https://www.acmicpc.net/problem/1167
from collections import deque

N = int(input())
A = [[] for _ in range(N + 1)]

for i in range(N):
    Data = list(map(int, input().split()))
    index = 0
    S = Data[index]
    index += 1
    while True:
        E = Data[index]
        if E == -1:
            break
        V = Data[index + 1]
        A[S].append((E, V))
        index += 2

distance = [0] * (N + 1)
visited = [False] * (N + 1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now_Node] + i[1]  # 거리 리스트 업데이트

BFS(1)
Max = 1

for i in range(2, N + 1):
    if distance[Max] < distance[i]:
        Max = i     # 거리 리스트값 중 Max값으로 시작점 재설정

distance = [0] * (N + 1)
visited = [False] * (N + 1)
BFS(Max)
distance.sort()
print(distance[N])