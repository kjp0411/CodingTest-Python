# https://www.acmicpc.net/problem/1325
# # 코드1 (시간 초과)
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# N, M = map(int, input().split())  # 노드의 수, 엣지의 수
# A = [[] for _ in range(N + 1)]
# answer = [0] * (N + 1)
#
# def BFS(v):
#     visited = [False] * (N + 1)
#     queue = deque()
#     queue.append(v)
#     visited[v] = True
#     while queue:
#         now_Node = queue.popleft()
#         for i in A[now_Node]:
#             if not visited[i]:
#                 visited[i] = True
#                 answer[i] += 1  # 신규 노드 인덱스의 정답 리스트값을 증가
#                 queue.append(i)
#
# for _ in range(M):
#     S, E = map(int, input().split())
#     A[S].append(E)
#
# for i in range(N + 1):          # 모든 노드에서 BFS 실행
#     BFS(i)
#
# max_value = max(answer)
#
# for i in range(1, N + 1):
#     if max_value == answer[i]:
#         print(i, end=' ')

# 코드2 (SCC + DAG + Bitset DP)
import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

N, M = map(int, input().split())

# 역방향 그래프: b -> a  (b를 해킹하면 a로 전파)
G  = [[] for _ in range(N + 1)]
GT = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[b].append(a)   # 역방향
    GT[a].append(b)  # G의 전치 (원래 방향)

# 1) Kosaraju: 역그래프 G와 그 전치 GT로 SCC 분해
visited = [False] * (N + 1)
order = []

def dfs1(u: int):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            dfs1(v)
    order.append(u)

for i in range(1, N + 1):
    if not visited[i]:
        dfs1(i)

comp = [-1] * (N + 1)
cid = 0

def dfs2(u: int, c: int):
    comp[u] = c
    for v in GT[u]:
        if comp[v] == -1:
            dfs2(v, c)

for u in reversed(order):
    if comp[u] == -1:
        dfs2(u, cid)
        cid += 1

K = cid  # SCC 개수

# 2) SCC DAG 구성 (중복 간선 제거)
CG = [set() for _ in range(K)]
members = [[] for _ in range(K)]
for u in range(1, N + 1):
    cu = comp[u]
    members[cu].append(u)
    for v in G[u]:
        cv = comp[v]
        if cu != cv:
            CG[cu].add(cv)

# 3) 각 컴포넌트의 기본 비트셋 (원래 노드 1..N -> 비트 0..N-1)
base = [0] * K
for c in range(K):
    bs = 0
    for u in members[c]:
        bs |= (1 << (u - 1))
    base[c] = bs

# 4) DAG 위상 순서 (dfs로 post-order 수집 → 자식이 앞)
visited_c = [0] * K
topo = []
def dfs_c(u: int):
    visited_c[u] = 1
    for v in CG[u]:
        if not visited_c[v]:
            dfs_c(v)
    topo.append(u)

for c in range(K):
    if not visited_c[c]:
        dfs_c(c)

# 중요: topo는 이미 "자식 먼저" 순서
# => 이 순서대로 올라오면서 OR 전파해야 함 (reversed 쓰면 오답!)
reach = [0] * K
for c in topo:
    r = base[c]
    for v in CG[c]:
        r |= reach[v]
    reach[c] = r

# 5) 각 정점 s의 해킹 가능 수 계산
cnt = [0] * (N + 1)
mx = 0
for s in range(1, N + 1):
    val = reach[comp[s]].bit_count()
    cnt[s] = val
    if val > mx:
        mx = val

# 6) 최대값 가진 정점들 출력
print(*[i for i in range(1, N + 1) if cnt[i] == mx])