# https://www.acmicpc.net/problem/22954
import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)

for idx in range(1, M + 1):
    a, b = map(int, input().split())
    graph[a].append((b, idx))
    graph[b].append((a, idx))

visited = [False] * (N + 1)

def dfs_component(start):
    stack = [start]
    visited[start] = True

    nodes = []
    tree_edges = []
    parent = {start: 0}
    child_count = defaultdict(int)

    while stack:
        cur = stack.pop()
        nodes.append(cur)

        for nxt, edge_idx in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                parent[nxt] = cur
                child_count[cur] += 1
                tree_edges.append(edge_idx)
                stack.append(nxt)

    return nodes, tree_edges, parent, child_count


components = []
for v in range(1, N + 1):
    if not visited[v]:
        components.append(dfs_component(v))

# 컴포넌트가 3개 이상이면 두 트리로 못 나눔
if len(components) >= 3:
    print(-1)
    sys.exit()

# 컴포넌트가 2개면 각 컴포넌트의 스패닝 트리를 그대로 사용
if len(components) == 2:
    nodes1, edges1, _, _ = components[0]
    nodes2, edges2, _, _ = components[1]

    if len(nodes1) == len(nodes2):
        print(-1)
    else:
        print(len(nodes1), len(nodes2))
        print(*nodes1)
        print(*edges1)
        print(*nodes2)
        print(*edges2)
    sys.exit()

# 여기부터 컴포넌트 1개
nodes, tree_edges, parent, child_count = components[0]

# 두 개의 서로 다른 크기 트리로 나누려면 최소 정점 수가 3개여야 함
if N <= 2:
    print(-1)
    sys.exit()

# DFS 스패닝 트리에서 leaf 하나 떼면 됨
# leaf 하나 = 크기 1의 트리, 나머지 = 크기 N-1의 트리
leaf = -1
for v in nodes:
    if parent[v] != 0 and child_count[v] == 0:
        leaf = v
        break

# 이 경우는 N>=2 트리에서 항상 존재해야 함
if leaf == -1:
    print(-1)
    sys.exit()

# leaf와 parent[leaf]를 잇는 트리 간선 번호 찾기
cut_edge = -1
p = parent[leaf]
for nxt, edge_idx in graph[leaf]:
    if nxt == p:
        cut_edge = edge_idx
        break

nodes1 = [leaf]
edges1 = []

nodes2 = [v for v in nodes if v != leaf]
edges2 = [e for e in tree_edges if e != cut_edge]

# 크기 확인
if len(nodes1) == len(nodes2):
    print(-1)
else:
    print(len(nodes1), len(nodes2))
    print(*nodes1)
    print(*edges1)
    print(*nodes2)
    print(*edges2)