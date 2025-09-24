# https://www.acmicpc.net/problem/1916
import sys
input = sys.stdin.readline
from queue import PriorityQueue

N = int(input())
M = int(input())
myList = [[] for _ in range(N + 1)]
distance = [sys.maxsize] * (N + 1)
visited = [False] * (N + 1)

for _ in range(M):
    s, e, w = map(int, input().split())     # 가중치가 있는 인접 리스트 저장
    myList[s].append((e, w))

start_index, end_index = map(int, input().split())

def dijkstra(s, e):
    pq = PriorityQueue()
    pq.put((0, s))
    # 우선순위에 데이터를 최단 거리, 노드 순으로 삽입
    distance[s] = 0
    while pq.qsize() > 0:
        nowNode = pq.get()
        now = nowNode[1]
        if not visited[now]:
            visited[now] = True
            for n in myList[now]:
                if distance[n[0]] > distance[now] + n[1]:
                    distance[n[0]] = distance[now] + n[1]
                    pq.put((distance[n[0]], n[0]))

    return distance[e]

print(dijkstra(start_index, end_index))