# https://www.acmicpc.net/problem/1197
# # 코드1 (런타임 에러)
# import sys
# from queue import PriorityQueue
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# pq = PriorityQueue()
# parent = [0] * (N + 1)
#
# for i in range(N + 1):
#     parent[i] = i
#
# for i in range(M):
#     s, e, w = map(int, input().split())
#     pq.put((w, s, e))   # 순서대로 정렬되므로 가중치를 제일 앞 순서로 함
#
# def find(a):
#     if a == parent[a]:
#         return a
#     else:
#         parent[a] = find(parent[a])
#         return parent[a]
#
# def union(a, b):
#     a = find(a)
#     b = find(b)
#     if a != b:
#         parent[b] = a
#
# useEdge = 0
# result = 0
#
# while useEdge < N - 1:      # 최소 신장 트리는 항상 N - 1의 엣지를 사용
#     w, s, e = pq.get()
#     if find(s) != find(e):  # 같은 부모가 아닌 경우만 연결
#         union(s, e)
#         result += w
#         useEdge += 1
#
# print(result)

# 코드 2
import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
for _ in range(M):
    s, e, w = map(int, input().split())
    edges.append((w, s, e))

heapq.heapify(edges)  # 가중치 기준 최소힙

parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])  # 경로 압축
    return parent[a]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    # union by rank
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True

useEdge = 0
result = 0

# 힙이 빌 수도 있으니 조건 두 개 모두 검사
while edges and useEdge < N - 1:
    w, s, e = heapq.heappop(edges)
    if union(s, e):
        result += w
        useEdge += 1

print(result)