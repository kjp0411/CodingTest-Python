# https://www.acmicpc.net/problem/14890
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def can_build(line, L):
    N = len(line)
    used = [False] * N

    for i in range(N - 1):
        if line[i] == line[i + 1]:
            continue

        diff = line[i + 1] - line[i]
        if abs(diff) > 1:
            return False

        if diff == 1:  # 올라가는 경사로
            h = line[i]
            for j in range(i, i - L, -1):
                if j < 0 or line[j] != h or used[j]:
                    return False
                used[j] = True

        elif diff == -1:  # 내려가는 경사로
            h = line[i + 1]
            for j in range(i + 1, i + 1 + L):
                if j >= N or line[j] != h or used[j]:
                    return False
                used[j] = True

    return True

ans = 0

# 1. 가로줄 검사
for r in range(N):
    if can_build(board[r], L):
        ans += 1

# 2. 세로줄 검사
for c in range(N):
    col = [board[r][c] for r in range(N)]
    if can_build(col, L):
        ans += 1

print(ans)