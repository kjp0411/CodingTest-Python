# https://www.acmicpc.net/problem/2169
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[-10**15] * M for _ in range(N)]

# 첫 행 (오른쪽으로만 이동 가능)
dp[0][0] = board[0][0]
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + board[0][j]

for i in range(1, N):

    left = [0] * M
    right = [0] * M

    # 왼쪽 -> 오른쪽
    left[0] = dp[i-1][0] + board[i][0]
    for j in range(1, M):
        left[j] = max(dp[i-1][j], left[j-1]) + board[i][j]

    # 오른쪽 -> 왼쪽
    right[M-1] = dp[i-1][M-1] + board[i][M-1]
    for j in range(M-2, -1, -1):
        right[j] = max(dp[i-1][j], right[j+1]) + board[i][j]

    for j in range(M):
        dp[i][j] = max(left[j], right[j])

print(dp[N-1][M-1])