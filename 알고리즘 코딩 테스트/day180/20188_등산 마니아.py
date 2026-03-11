# https://www.acmicpc.net/problem/20188
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N + 1)
subtree = [1] * (N + 1)

# 재귀 대신 반복 DFS
stack = [1]
order = []

while stack:
    cur = stack.pop()
    order.append(cur)
    for nxt in graph[cur]:
        if nxt == parent[cur]:
            continue
        parent[nxt] = cur
        stack.append(nxt)

# 후위 순회처럼 subtree 크기 계산
while order:
    cur = order.pop()
    if parent[cur] != 0:
        subtree[parent[cur]] += subtree[cur]

def comb2(x):
    return x * (x - 1) // 2

total_pairs = comb2(N)
answer = 0

for i in range(2, N + 1):
    s = subtree[i]
    answer += total_pairs - comb2(N - s)

print(answer)