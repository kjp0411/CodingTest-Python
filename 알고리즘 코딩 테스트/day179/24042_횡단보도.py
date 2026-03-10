# https://www.acmicpc.net/problem/24042
import sys
import heapq

input = sys.stdin.readline
INF = 10**18

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append((B, i))
    graph[B].append((A, i))

dist = [INF] * (N+1)
dist[1] = 0

pq = []
heapq.heappush(pq, (0, 1))

while pq:
    time, now = heapq.heappop(pq)

    if time > dist[now]:
        continue

    for next_node, edge_idx in graph[now]:

        wait = (edge_idx - (time % M) + M) % M
        next_time = time + wait + 1

        if next_time < dist[next_node]:
            dist[next_node] = next_time
            heapq.heappush(pq, (next_time, next_node))

print(dist[N])