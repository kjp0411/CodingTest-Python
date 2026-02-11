# https://www.acmicpc.net/problem/2533
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
dp = [[0, 0] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

def dfs(u, parent):
    dp[u][0] = 0
    dp[u][1] = 1

    for v in tree[u]:
        if v == parent:
            continue
        dfs(v, u)

        # u를 선택한 경우(u는 얼리 아답터)
        dp[u][1] += min(dp[v][0], dp[v][1])

        # u를 선택하지 않은 경우(모든 자식v는 얼리 아답터)
        dp[u][0] += dp[v][1]

dfs(1, 0)
print(min(dp[1][0], dp[1][1]))