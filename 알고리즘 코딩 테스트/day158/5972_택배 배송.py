# https://www.acmicpc.net/problem/5972
import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

INF = 10**18
dist = [INF] * (N+1)
dist[1] = 0

heap = [(0, 1)]

while heap:
    cost, node = heapq.heappop(heap)

    if cost > dist[node]:
        continue

    for nxt, w in graph[node]:
        ncost = cost + w
        if ncost < dist[nxt]:
            dist[nxt] = ncost
            heapq.heappush(heap, (ncost, nxt))

print(dist[N])