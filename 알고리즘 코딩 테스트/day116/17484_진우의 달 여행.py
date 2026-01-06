# https://www.acmicpc.net/problem/17484
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
INF = 10**9
dp = [[[INF, INF, INF] for _ in range(M)] for _ in range(N)]
dc = [-1, 0, 1]

for c in range(M):
    for d in range(3):
        dp[0][c][d] = matrix[0][c]

for r in range(1, N):
    for c in range(M):
        for d in range(3):
            nc = c + dc[d]
            if 0 <= nc < M:
                for prev_d in range(3):
                    if prev_d != d:
                        dp[r][c][d] = min(
                            dp[r][c][d],
                            dp[r-1][nc][prev_d] + matrix[r][c]
                        )

low_cost = INF
for c in range(M):
    for d in range(3):
        if low_cost > dp[N-1][c][d]:
            low_cost = dp[N-1][c][d]
print(low_cost)