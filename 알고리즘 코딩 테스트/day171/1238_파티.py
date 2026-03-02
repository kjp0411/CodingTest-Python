# https://www.acmicpc.net/problem/1238
import heapq
import sys
input = sys.stdin.readline
INF = 10**15

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
rev_graph = [[] for _ in range(N+1)]

for _ in range(M):
    S, E, T = map(int, input().split())
    graph[S].append((E, T))
    rev_graph[E].append((S, T))

def dijkstra(start, graph):
    dist = [INF] * (N+1)
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cost, now = heapq.heappop(pq)

        if cost > dist[now]:
            continue

        for next_node, next_cost in graph[now]:
            new_cost = cost + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
    return dist

dist_from_X = dijkstra(X, graph)
dist_to_X = dijkstra(X, rev_graph)

answer = 0
for i in range(1, N+1):
    answer = max(answer, dist_from_X[i] + dist_to_X[i])

print(answer)