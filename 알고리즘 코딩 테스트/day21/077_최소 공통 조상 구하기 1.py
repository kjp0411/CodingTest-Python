# https://www.acmicpc.net/problem/11437
# # 코드1 (시간 초과)
# import sys
# input = sys.stdin.readline
# N = int(input())
# tree = [[] for _ in range(N + 1)]
#
# for i in range(0, N - 1):   # 인접 리스트에 트리 데이터 저장
#     s, e = map(int, input().split())
#     tree[s].append(e)
#     tree[e].append(s)
#
# depth = [0] * (N + 1)
# parent = [0] * (N + 1)
# visited = [False] * (N + 1)
#
# def BFS(node):
#     queue = [node]
#     visited[node] = True
#     while queue:
#         now_node = queue.pop(0)
#         for next in tree[now_node]:
#             if not visited[next]:
#                 visited[next] = True
#                 queue.append(next)
#                 parent[next] = now_node             # 부모 노드 저장
#                 depth[next] = depth[now_node] + 1   # 노드 depth 저장
#
# BFS(1)
#
# def excuteLCA(a, b):
#     if depth[a] < depth[b]:
#         temp = a
#         a = b
#         b = temp
#
#     while depth[a] != depth[b]:
#         a = parent[a]
#
#     while a != b:
#         a = parent[a]
#         b = parent[b]
#
#     return a
#
# M = int(input())
# mydict = dict()
# for i in range(M):
#     a, b = map(int, input().split())
#     if not mydict.get((a, b), 0):   # 같은 질문일 경우 재계산을 하지 않기 위해 딕셔너리 자료형 사용
#         mydict[(a, b)] = mydict[(b, a)] = excuteLCA(a, b)
#     print(mydict.get((a, b)))

# 코드 2(deque + binary lifting)
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

# BFS로 depth와 1단계 부모(parent[0])
LOG = (N).bit_length()  # ceil(log2(N+1))
parent = [[0] * (N + 1) for _ in range(LOG)]  # parent[k][v] = v의 2^k번째 조상
depth = [0] * (N + 1)
visited = [False] * (N + 1)

def BFS(root: int = 1):
    dq = deque([root])
    visited[root] = True
    depth[root] = 0
    parent[0][root] = 0  # 루트의 부모는 0
    while dq:
        now = dq.popleft()
        for nxt in tree[now]:
            if not visited[nxt]:
                visited[nxt] = True
                depth[nxt] = depth[now] + 1
                parent[0][nxt] = now
                dq.append(nxt)

BFS(1)

# parent 테이블 전처리 (이진 점프)
for k in range(1, LOG):
    prev = parent[k - 1]
    cur = parent[k]
    for v in range(1, N + 1):
        cur[v] = prev[prev[v]]  # parent[k][v] = parent[k-1][ parent[k-1][v] ]

def lca(a: int, b: int) -> int:
    # 깊이 맞추기 (a가 더 깊거나 같도록)
    if depth[a] < depth[b]:
        a, b = b, a
    diff = depth[a] - depth[b]
    bit = 0
    while diff:
        if diff & 1:
            a = parent[bit][a]
        diff >>= 1
        bit += 1
    if a == b:
        return a
    # 가장 높은 레벨부터 내려오며 공통 부모 직전까지 점프
    for k in range(LOG - 1, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]
    return parent[0][a]

M = int(input())
out = []
for _ in range(M):
    a, b = map(int, input().split())
    out.append(str(lca(a, b)))

print("\n".join(out))