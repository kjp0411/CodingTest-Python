# https://www.acmicpc.net/problem/2213
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
weight = [0] + list(map(int, input().split()))
dp = [[0, 0] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

def dfs(u, parent) :
    dp[u][0] = 0
    dp[u][1] = weight[u]

    for v in tree[u]:
        if v == parent:
            continue
        dfs(v, u)

        # u를 선택한 경우
        dp[u][1] += dp[v][0]

        # u를 선택하지 않은 경우
        dp[u][0] += max(dp[v][0], dp[v][1])

dfs(1, 0)
print(max(dp[1][0], dp[1][1]))

result = []

def trace(u, parent, take):
    if take:
        result.append(u)

    for v in tree[u]:
        if v == parent:
            continue

        if take:
            # u를 선택한 경우
            trace(v, u, False)
        else:
            # u를 선택하지 않은 경우
            if dp[v][1] > dp[v][0]:
                trace(v, u, True)
            else:
                trace(v, u, False)

if dp[1][1] > dp[1][0]:
    trace(1, 0, True)
else:
    trace(1, 0, False)

result.sort()
print(*result)